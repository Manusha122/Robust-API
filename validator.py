import re
from datetime import datetime

def is_valid_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

def is_valid_iso8601(timestamp):
    try:
        datetime.fromisoformat(timestamp.replace("Z", "+00:00"))
        return True
    except ValueError:
        return False

def validate_item(item):
    errors = []
    if not item.get("item_id"):
        errors.append("Item ID is required.")
    if not isinstance(item.get("quantity"), int) or item["quantity"] <= 0:
        errors.append("Quantity must be > 0.")
    if not isinstance(item.get("price"), float) or item["price"] <= 0:
        errors.append("Price must be a positive float.")
    return errors

def validate_data(data):
    all_errors = []

    if not isinstance(data, list):
        return False, ["Data must be a list"]

    for i, entry in enumerate(data):
        entry_errors = []

        if not entry.get("user_id"):
            entry_errors.append("user_id is required and must be non-empty.")
        if not is_valid_email(entry.get("email", "")):
            entry_errors.append("Invalid email format.")
        if not is_valid_iso8601(entry.get("timestamp", "")):
            entry_errors.append("Invalid timestamp format (ISO 8601 expected).")
        if not isinstance(entry.get("items"), list) or not entry["items"]:
            entry_errors.append("Items must be a non-empty list.")
        else:
            for item in entry["items"]:
                entry_errors.extend(validate_item(item))

        if entry_errors:
            all_errors.append({f"Record {i}": entry_errors})

    return (len(all_errors) == 0), all_errors
