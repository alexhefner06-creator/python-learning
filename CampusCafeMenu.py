print("==============================")
print("CAMPUS CAFÉ ORDER SYSTEM")
print("==============================")
print("1. Coffee - $3.50")
print("2. Sandwich - $6.00")
print("3. Salad - $5.50")
print("4. Combo - $8.00")
print("5. Exit")
print("==============================")

choice = input("Enter your choice (1-5): ")

item_name = ""
unit_price = 0

# Coffee
if choice == "1":
    item_name = "Coffee"
    size = input("Choose size (small/medium/large): ").lower()

    if size == "medium":
        unit_price = 4.50
        item_name += " (Medium)"
    elif size == "large":
        unit_price = 5.50
        item_name += " (Large)"
    else:
        unit_price = 3.50
        item_name += " (Small)"
        if size != "small":
            print("Invalid size. Defaulting to Small.")

# Sandwich
elif choice == "2":
    item_name = "Sandwich"
    unit_price = 6.00
    cheese = input("Add cheese? (yes/no): ").lower()

    if cheese == "yes":
        unit_price += 0.75
        item_name += " + Cheese"

# Salad
elif choice == "3":
    item_name = "Salad"
    unit_price = 5.50
    dressing = input("Choose dressing (ranch/italian/vinaigrette/none): ").lower()

    if dressing in ["ranch", "italian", "vinaigrette", "none"]:
        if dressing != "none":
            item_name += f" ({dressing.capitalize()} dressing)"
    else:
        print("Invalid dressing. Defaulting to none.")

# Combo
elif choice == "4":
    item_name = "Combo (Sandwich + Coffee)"
    unit_price = 8.00

    # Coffee size
    size = input("Choose coffee size (small/medium/large): ").lower()
    if size == "medium":
        unit_price += 1.00
        item_name += " + Medium Coffee"
    elif size == "large":
        unit_price += 2.00
        item_name += " + Large Coffee"
    else:
        item_name += " + Small Coffee"
        if size != "small":
            print("Invalid size. Defaulting to Small.")

    # Cheese option
    cheese = input("Add cheese to sandwich? (yes/no): ").lower()
    if cheese == "yes":
        unit_price += 0.75
        item_name += " + Cheese"

elif choice == "5":
    print("Goodbye!")
    exit()

else:
    print("Invalid menu choice.")
    exit()

# Name validation
name = input("Enter your name: ").strip()
if name == "":
    print("Name cannot be empty.")
    exit()

# Quantity validation
try:
    quantity = int(input("How many? "))
    if quantity <= 0:
        print("Quantity must be a positive integer.")
        exit()
except:
    print("Invalid quantity.")
    exit()

# Calculations
subtotal = unit_price * quantity
tax = subtotal * 0.07
total = subtotal + tax

# Receipt
print("==============================")
print("ORDER RECEIPT")
print("==============================")
print(f"Customer: {name}")
print(f"Item: {item_name}")
print(f"Quantity: {quantity}")
print(f"Unit Price: ${unit_price:.2f}")
print(f"Subtotal: ${subtotal:.2f}")
print(f"Tax (7%): ${tax:.2f}")
print(f"Total: ${total:.2f}")
print("==============================")
print("Thank you for your order!")