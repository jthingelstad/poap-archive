"""Harvest everything POAP Compass still serves about Jamie's POAP life."""
import json, os, re, sys, time, urllib.request
OUT = sys.argv[1]; EMAIL = sys.argv[2]; DROP_IDS = [int(x) for x in sys.argv[3].split(",")]; ADDRS = [a.lower() for a in sys.argv[4:]]
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
def save(name, data):
    json.dump(data, open(f"{OUT}/{name}.json", "w"), indent=2); print(f"{name}: {len(data) if isinstance(data, list) else 'ok'}")
os.makedirs(OUT, exist_ok=True)
DROP = f"{scalars('drops')} email_claims_stats {{ {scalars('email_claims_stats')} }} drop_image {{ {scalars('drop_images')} gateways {{ {scalars('drop_image_gateways')} }} }}"
TRANSFER = scalars("transfers")
MOMENT = f"{scalars('moments')} media {{ {scalars('moment_media')} }} links {{ {scalars('moments_links')} }}"
POAP = scalars("poaps")
# 1. tokens Jamie holds, with full drop record and transfer history
save("collected", paged("poaps", {"collector_address": {"_in": ADDRS}}, f"{POAP} drop {{ {DROP} }} transfers(order_by:{{timestamp: asc}}) {{ {TRANSFER} }}"))
# 2. every transfer in or out of Jamie's wallets (catches tokens given away or moved)
save("transfers", paged("transfers", {"_or": [{"from_address": {"_in": ADDRS}}, {"to_address": {"_in": ADDRS}}]}, f"{TRANSFER} poap {{ id drop_id drop {{ name }} }}"))
# 3. drops Jamie created: full record plus every token minted
created = paged("drops", {"id": {"_in": DROP_IDS}}, DROP)
save("created_drops", created)
holders = paged("poaps", {"drop_id": {"_in": DROP_IDS}}, f"{POAP} transfers(order_by:{{timestamp: asc}}) {{ {TRANSFER} }}")
save("created_drop_tokens", holders)
# 4. moments (photos/notes) on Jamie's drops or by Jamie
save("moments", paged("moments", {"_or": [{"drop_id": {"_in": DROP_IDS}}, {"author": {"_in": ADDRS}}]}, MOMENT))
# 5. collections Jamie made or owns
save("collections", paged("collections", {"_or": [{"owner_address": {"_in": ADDRS}}, {"created_by": {"_in": ADDRS}}]}, f"{scalars('collections')} collections_items {{ {scalars('items')} }}"))
# 6. drops reserved to Jamie's email but never minted
save("email_reservations", q(f'query($e:String){{ reserved_drops_by_email(args:{{email:$e}}) {{ drop_id reserved_at drop {{ {DROP} }} }} }}', {"e": EMAIL})["reserved_drops_by_email"])
# 7. per-address stats
save("collector_stats", q(f'query($a:[String!]){{ collectors_stats_by_chain(where:{{address:{{_in:$a}}}}) {{ {scalars("collectors_stats_by_chain")} }} }}', {"a": ADDRS})["collectors_stats_by_chain"])
