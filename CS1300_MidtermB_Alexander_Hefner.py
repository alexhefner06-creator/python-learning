#BMI Calculator
weight = float(input("Enter weight: "))
unit = input("Enter unit system (M/I): ")

if unit.lower() == "m":
    height = float(input("Enter height (meters): "))
    bmi = weight / (height ** 2)

elif unit.lower() == "i":
    height = float(input("Enter height (inches): "))
    bmi = (weight * 703) / (height ** 2)

else:
    print("Invalid unit system.")
    exit()

print(f"BMI: {bmi:.1f}")

if bmi < 18.5:
    category = "Underweight"
elif bmi <= 24.9:
    category = "Normal weight"
elif bmi <= 29.9:
    category = "Overweight"
else:
    category = "Obese"

print("Category:", category)


#Password Strength Checker
password = input("Enter a password: ")

length_ok = len(password) >= 8
has_upper = False
has_lower = False
has_digit = False
has_special = False

for char in password:
    if char.isupper():
        has_upper = True
    elif char.islower():
        has_lower = True
    elif char.isdigit():
        has_digit = True
    else:
        has_special = True

print("Length >= 8:", "PASS" if length_ok else "FAIL")
print("Uppercase:", "PASS" if has_upper else "FAIL")
print("Lowercase:", "PASS" if has_lower else "FAIL")
print("Digit:", "PASS" if has_digit else "FAIL")
print("Special char:", "PASS" if has_special else "FAIL")

criteria_met = sum([length_ok, has_upper, has_lower, has_digit, has_special])
print(f"Criteria met: {criteria_met} / 5")

if len(password) == 0:
    strength = "No password entered"
elif criteria_met == 5:
    strength = "Strong"
elif criteria_met >= 3:
    strength = "Moderate"
elif criteria_met >= 1:
    strength = "Weak"
else:
    strength = "No password entered"

print("Strength:", strength)


#Invetory Manager
products = ["Laptop", "Mouse", "Keyboard", "Monitor", "Headset"]
quantities = [12, 45, 30, 8, 22]

print("=== INVENTORY ===")
for i in range(len(products)):
    print(f"{i+1}. {products[i]} - {quantities[i]}")
print("=================")

highest = quantities[0]
lowest = quantities[0]
high_index = 0
low_index = 0

for i in range(len(quantities)):
    if quantities[i] > highest:
        highest = quantities[i]
        high_index = i
    if quantities[i] < lowest:
        lowest = quantities[i]
        low_index = i

print(f"Highest: {products[high_index]} ({highest})")
print(f"Lowest: {products[low_index]} ({lowest})")

total = 0
for q in quantities:
    total += q

average = total / len(quantities)

print("Total quantity:", total)
print(f"Average quantity: {average:.2f}")

products.append("Webcam")
quantities.append(15)

print("\nAfter appending Webcam:")
for i in range(len(products)):
    print(f"{i+1}. {products[i]} - {quantities[i]}")

products.insert(2, "USB Hub")
quantities.insert(2, 50)

print("\nAfter inserting USB Hub:")
for i in range(len(products)):
    print(f"{i+1}. {products[i]} - {quantities[i]}")

idx = products.index("Headset")
products.pop(idx)
quantities.pop(idx)

print("\nAfter removing Headset:")
for i in range(len(products)):
    print(f"{i+1}. {products[i]} - {quantities[i]}")

removed_product = products.pop()
removed_quantity = quantities.pop()

print("\nPopped item:", removed_product, "-", removed_quantity)

print("\n=== FINAL INVENTORY ===")
for i in range(len(products)):
    print(f"{i+1}. {products[i]} - {quantities[i]}")

print("Length:", len(products))


#Parking Fee Calculator
vehicle = input("Enter vehicle type (car/motorcycle/truck): ")
hours = float(input("Enter hours parked: "))
pass_holder = input("Monthly pass? (yes/no): ")

vehicle = vehicle.lower()
pass_holder = pass_holder.lower()

if vehicle not in ["car", "motorcycle", "truck"]:
    print("Invalid vehicle type.")
else:
    if pass_holder == "yes":
        fee = 0.0
    elif vehicle == "motorcycle":
        if hours <= 2:
            fee = 1.00
        else:
            fee = 1.00 + (hours - 2) * 0.50
    elif vehicle == "car":
        if hours <= 2:
            fee = 3.00
        else:
            fee = 3.00 + (hours - 2) * 1.50
    elif vehicle == "truck":
        if hours <= 2:
            fee = 5.00
        else:
            fee = 5.00 + (hours - 2) * 2.50

    print("--- Parking Receipt ---")
    print("Vehicle:", vehicle.capitalize())
    print(f"Duration: {hours:.2f} hours")
    print("Pass holder:", pass_holder.capitalize())
    print(f"Fee: ${fee:.2f}")
    print("-----------------------")


#Word Frequency Counter
sentence = input("Enter a sentence: ")

words = sentence.lower().split()

print("Total words:", len(words))

unique_words = []
for w in words:
    if w not in unique_words:
        unique_words.append(w)

print("Unique words:", unique_words)

print("--- Word Frequencies ---")

most_word = ""
most_count = 0

for w in unique_words:
    count = words.count(w)
    print(f"{w}: {count}")
    if count > most_count:
        most_count = count
        most_word = w

print(f'Most frequent word: "{most_word}" ({most_count} times)')