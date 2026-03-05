first_name = input("Enter your first name: ").title()
last_name = input("Enter your last name: ").title()
birth_year = int(input("Enter your birth year: "))
hobby = input("Enter your favorite hobby: ").title()
current_year = 2026
age = current_year - birth_year
border = "=" * 36
line = "-" * 36
print(border)
print("USER PROFILE CARD")
print(border)
print(f"Name: {first_name} {last_name}")
print(f"Age: {age}")
print(f"Hobby: {hobby}")
print(line)
print("Thank you for creating your profile!")
print(border)