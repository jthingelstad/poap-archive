"""Shared POAP Compass GraphQL helpers."""
import json, time, urllib.request
URL = "https://public.compass.poap.tech/v1/graphql"
def q(query, variables=None):
    body = json.dumps({"query": query, "variables": variables or {}}).encode()
    for i in range(5):
        try:
            r = urllib.request.urlopen(urllib.request.Request(URL, body, {"content-type": "application/json", "User-Agent": "jamie-poap-archive/1.0"}), timeout=120)
            d = json.loads(r.read())
            if "errors" in d: raise RuntimeError(d["errors"])
            return d["data"]
        except RuntimeError: raise
        except Exception as e: err = e; time.sleep(2 ** i)
    raise err
_types = {}
def scalars(t):
    if t not in _types:
        d = q('query($n:String!){ __type(name:$n){ fields { name args { name } type { kind ofType { kind ofType { kind } } } } } }', {"n": t})["__type"]
        def leaf(ty):
            while ty and ty["kind"] == "NON_NULL": ty = ty.get("ofType")
            return ty and ty["kind"] in ("SCALAR", "ENUM")
        _types[t] = " ".join(f["name"] for f in d["fields"] if leaf(f["type"]) and not f["args"])
    return _types[t]
def paged(field, where, sel, order="{id: asc}", page=100):
    rows, off = [], 0
    while True:
        d = q(f'query($w:{field}_bool_exp,$o:Int){{ {field}(where:$w, limit:{page}, offset:$o, order_by:{order}) {{ {sel} }} }}', {"w": where, "o": off})[field]
        rows += d; off += page
        if len(d) < page: return rows
