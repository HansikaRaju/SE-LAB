"""E-commerce cart system with static-analysis improvements."""

import hashlib
import secrets


cart_items = {
    "ITEM1": {"name": "Wireless Mouse", "price": 25.0, "qty": 2},
    "ITEM2": {"name": "Mechanical Keyboard", "price": 80.0, "qty": 1},
    "ITEM3": {"name": "USB-C Hub", "price": 45.0, "qty": 3},
}

total_sales = 0.0


def add_item_to_cart(item_id, name, price, qty=1, audit_log=None):
    """Add an item to the shopping cart."""
    global total_sales

    if audit_log is None:
        audit_log = []

    if item_id in cart_items:
        return False

    cart_items[item_id] = {
        "name": name,
        "price": price,
        "qty": qty,
    }

    total_sales += price * qty
    audit_log.append(f"Added {item_id} with price {price:.2f}")
    return True


def remove_item_from_cart(item_id):
    """Remove an item from the shopping cart."""
    if item_id in cart_items:
        del cart_items[item_id]


def check_cart_status(item_id):
    """Check whether an item is available in the cart."""
    item = cart_items.get(item_id)

    if item is None:
        return False

    return item["qty"] > 0


def calculate_discounted_total(item_id, discount_rate):
    """Calculate the discounted price of an item."""
    base_price = cart_items[item_id]["price"]
    return base_price * discount_rate


def generate_item_hash(item_id):
    """Generate a SHA-256 hash for an item ID."""
    return hashlib.sha256(item_id.encode()).hexdigest()


def generate_checkout_pin():
    """Generate a secure four-digit checkout PIN."""
    return secrets.randbelow(9000) + 1000


def export_cart_receipt(filename="receipt.txt"):
    """Save the current cart to a receipt file."""
    with open(filename, "w", encoding="utf-8") as file:
        file.write(str(cart_items))

    print("Receipt saved to:", filename)


def get_cart_summary(items):
    """Return the total quantity of items in the cart."""
    total_items = 0

    for details in items.values():
        if details["qty"] > 0:
            total_items += details["qty"]

    return total_items


def main():
    """Run the e-commerce cart demonstration."""
    add_item_to_cart("ITEM4", "Monitor Stand", 35.0, 1)
    remove_item_from_cart("ITEM2")

    print("Is ITEM1 in cart:", check_cart_status("ITEM1"))
    print(
        "Discounted Price:",
        calculate_discounted_total("ITEM1", 0.90),
    )
    print("Item Hash:", generate_item_hash("ITEM1"))
    print("Checkout PIN:", generate_checkout_pin())
    export_cart_receipt()
    print("Total items:", get_cart_summary(cart_items))


if __name__ == "__main__":
    main()
