# Ask for user input
age = int(input("Enter your age: "))
matinee_input = input("Is this a matinee showing? (yes/no): ").lower()

# Convert yes/no to Boolean using a conditional expression
is_matinee = True if matinee_input == "yes" else False

# Validate age
if age < 0:
    print("Error: Age cannot be negative.")
else:
    # Determine age group
    if age < 13:
        age_group = "Child"
        if is_matinee:
            price = 6.00
        else:
            price = 8.00

    elif age <= 17:
        age_group = "Teen"
        if is_matinee:
            price = 7.00
        else:
            price = 10.00

    elif age <= 64:
        age_group = "Adult"
        if is_matinee:
            price = 8.00
        else:
            price = 13.00

    else:
        age_group = "Senior"
        if is_matinee:
            price = 6.00
        else:
            price = 7.00

    # Display results
    print(f"Age group: {age_group}")
    print(f"Ticket price: ${price:.2f}")