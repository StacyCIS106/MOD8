file_content = """Widget, 10, 50
Hammer, 2, 10
Saw, 4, 8 
Screwdriver, 1, 5
Chair, 3, 15
"""

with open("inventory.txt", "w") as file:
    file.write(file_content)

total_extended_price = 0
order_count = 0
with open("inventory.txt", "r") as file:
    print(f"{'item_name':<15} {'quantity':<10} {'unit_price':<12} {'extended_price':<15}")
    for line in file:
        item_name, quantity_str, unit_price_str = line.split(",")
        quantity = int(quantity_str)
        unit_price = float(unit_price_str)
        extended_price = quantity * unit_price
        total_extended_price += extended_price
        order_count += 1
        print(f"{item_name:<15} {quantity:<10} {unit_price:<12.2f} {extended_price:<15.2f}")
print(f"{'Total Orders:':<15} {order_count:<10} {'Total Extended Price:':<12} {total_extended_price:<15.2f}")
