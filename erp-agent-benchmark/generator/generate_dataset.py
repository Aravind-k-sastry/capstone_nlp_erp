import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "generated"
OUT.mkdir(exist_ok=True)

products = [
    {"name": "Motor A", "unit_price": 800},
    {"name": "Bearing B", "unit_price": 250}
]
suppliers = [
    {"name": "Vendor X", "approved": True},
    {"name": "Vendor Y", "approved": True}
]
users = [
    {"user_id": "U001", "role": "purchasing_manager"},
    {"user_id": "U002", "role": "sales_associate"}
]

rows = []
n = 1
for user in users:
    for product in products:
        for supplier in suppliers:
            for quantity in [10, 100, 1000]:
                amount = quantity * product["unit_price"]
                if user["role"] != "purchasing_manager":
                    decision = "DENY"
                elif amount > 500000:
                    decision = "REQUIRE_APPROVAL"
                else:
                    decision = "ALLOW"
                rows.append({
                    "request_id": f"REQ{n:04d}",
                    "user_id": user["user_id"],
                    "role": user["role"],
                    "natural_language_request":
                        f"Create a purchase order for {quantity} units of {product['name']} from {supplier['name']}.",
                    "expected_intent": "create_purchase_order",
                    "expected_parameters": {
                        "product": product["name"],
                        "quantity": quantity,
                        "supplier": supplier["name"]
                    },
                    "expected_decision": decision
                })
                n += 1

with open(OUT / "erp_agent_benchmark.json", "w", encoding="utf-8") as f:
    json.dump(rows, f, indent=2)

print(f"Generated {len(rows)} records: {OUT / 'erp_agent_benchmark.json'}")
