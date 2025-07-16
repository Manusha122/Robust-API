from concurrent.futures import ThreadPoolExecutor
from functools import reduce
from unittest import result

# Simulate map-reduce: sum total price for all items

def process_user_data(entry):
    total = 0
    for item in entry["items"]:
        total += item["quantity"] * item["price"]
    return {"user_id": entry["user_id"], "total_value": total}

def process_large_data(data):
    results = []
    with ThreadPoolExecutor(max_workers=4) as executor:
        futures = executor.map(process_user_data, data)
        results = list(futures)

# Simulate reduce: grand total
    grand_total = reduce(lambda acc, x: acc + x["total_value"], results, 0)
    return {
        "user_summaries": results,
        "grand_total": round(grand_total, 2)
    }

    