menu = {
    "Pizza": 150,
    "Pasta": 100,
    "Burger": 70,
    "Salad": 60,
    "Coffee": 100
}

print("Welcome to Python Restaurant")
print("-----MENU-----")
for item, price in menu.items():
    print(f"{item}: {price}")
print()

order_total = 0

def order_item(item_name):
    global order_total
    item_name = item_name.capitalize()  # Makes input case-insensitive
    if item_name in menu:
        order_total += menu[item_name]
        print(f"Your item {item_name} has been ordered.")
    else:
        print(f"{item_name} is not available.")

# First order
item1 = input("Enter the name of item you want to order: ")
order_item(item1)

# Loop for additional orders
while True:
    another_order = input("Do you want to add another item? (y/n): ").lower()
    if another_order == "y":
        item2 = input("Enter order: ")
        order_item(item2)
    else:
        break

print(f"The total amount is {order_total}")
