#Temp Converter
temp = float(input("Enter temperature: "))
scale = input("Enter scale (C/F): ").lower()

if scale == "c":
    f = temp * 9/5 + 32
    print(f"{temp:.1f}°C = {f:.1f}°F")
elif scale == "f":
    c = (temp - 32) * 5/9
    print(f"{temp:.1f}°F = {c:.1f}°C")
else:
    print("Invalid scale.")


#String Analyizer
sentence = input("Enter a sentence: ")

uppercase = 0
lowercase = 0
digits = 0
spaces = 0

for char in sentence:
    if char.isupper():
        uppercase += 1
    if char.islower():
        lowercase += 1
    if char.isdigit():
        digits += 1
    if char == " ":
        spaces += 1

print("Total characters:", len(sentence))
print("Uppercase letters:", uppercase)
print("Lowercase letters:", lowercase)
print("Digits:", digits)
print("Spaces:", spaces)
print("Reversed:", sentence[::-1])


#List Operations Toolkit
numbers = [15, 8, 23, 42, 4, 16, 31, 7, 19, 11]

# 1. Original list
print("Original:", numbers)

# 2. First and last elements
print(f"First: {numbers[0]}, Last: {numbers[len(numbers)-1]}")

# 3. Middle 4 elements (indices 3–6)
print("Middle 4:", numbers[3:7])

# 4. Append 99
numbers.append(99)
print("After append:", numbers)

# 5. Insert 0 at beginning
numbers.insert(0, 0)
print("After insert:", numbers)

# 6. Remove 42
numbers.remove(42)
print("After remove:", numbers)

# 7. Pop last element
removed = numbers.pop()
print("Popped value:", removed)
print("After pop:", numbers)

# 8. Check if 23 is in list
print("23 in list:", 23 in numbers)

# 9. Index of 16
print("Index of 16:", numbers.index(16))

# 10. Final list and length
print("Final list:", numbers)
print("Length:", len(numbers))


#Course Eligibility Checker
gpa = float(input("Enter GPA (0.0-4.0): "))
credits = int(input("Enter credit hours completed: "))
prereq_input = input("Prerequisite completed? (yes/no): ").lower()

prereq = prereq_input == "yes"

# Determine eligibility
if gpa >= 3.5 and credits >= 60 and prereq:
    status = "Approved: You meet all requirements."
elif gpa >= 3.5 and credits >= 60 and not prereq:
    status = "Conditionally approved: Complete the prerequisite first."
elif gpa >= 3.0 and credits >= 45:
    status = "Waitlisted: You may be admitted if space is available."
elif gpa >= 2.0:
    status = "Not eligible yet: Raise your GPA or earn more credits."
else:
    status = "Denied: GPA is below minimum threshold."

# Format prerequisite for display
prereq_text = "Yes" if prereq else "No"

# Summary report
print("--- Registration Summary ---")
print(f"GPA: {gpa:.2f}")
print(f"Credits: {credits}")
print(f"Prerequisite: {prereq_text}")
print(f"Status: {status}")
print("----------------------------")


#Student Roster Manager
names = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
scores = [88, 72, 95, 64, 81]

# Task 1: Print roster
print("=== CLASS ROSTER ===")
for i in range(len(names)):
    print(f"{i+1}. {names[i]} - {scores[i]}")
print("====================")

# Task 2: Highest and lowest score
highest_index = 0
lowest_index = 0

for i in range(1, len(scores)):
    if scores[i] > scores[highest_index]:
        highest_index = i
    if scores[i] < scores[lowest_index]:
        lowest_index = i

print("Highest score:", names[highest_index], "-", scores[highest_index])
print("Lowest score:", names[lowest_index], "-", scores[lowest_index])

# Task 3: Class average
total = 0
for score in scores:
    total += score

average = total / len(scores)
print(f"Class average: {average:.2f}")

# Task 4: Grade report
print("--- Grade Report ---")
for i in range(len(scores)):
    score = scores[i]

    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"

    print(f"{names[i]}: {score} -> {grade}")

# Task 5: Add Frank and remove Diana
names.append("Frank")
scores.append(77)

index = names.index("Diana")
names.pop(index)
scores.pop(index)

print("Updated roster length:", len(names))