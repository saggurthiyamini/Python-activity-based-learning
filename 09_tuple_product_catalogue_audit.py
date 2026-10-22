# Case Study 49: Tuple-Based Product Catalogue Audit

# Each product is stored as a tuple: (product_id, price, stock_quantity)
catalogue = (
    ("P101", 25.50, 20),
    ("P102", 0.00, 10),
    ("P103", 120.00, 0),
    ("P104", 75.00, 5),
    ("P105", -4.00, 8)
)

reorder_level = int(input("Enter reorder level: "))
inventory_value = 0
seen_ids = []

print("\n--- Product Catalogue Audit ---")
for product_id, price, quantity in catalogue:
    issues = []

    if product_id in seen_ids:
        issues.append("duplicate product ID")
    seen_ids.append(product_id)

    if price <= 0:
        issues.append("invalid price")
    if quantity < 0:
        issues.append("invalid stock quantity")

    if price > 0 and quantity >= 0:
        inventory_value += price * quantity

    if quantity <= reorder_level:
        issues.append("replenishment required")

    print(f"{product_id}: price={price:.2f}, stock={quantity}")
    print("  Status:", ", ".join(issues) if issues else "Valid")

print(f"\nTotal valid-record inventory value: Rs. {inventory_value:.2f}")
