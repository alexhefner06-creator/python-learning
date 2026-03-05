# Get student information
name = input("Enter student name: ")
exam1 = float(input("Enter Exam 1 score: "))
exam2 = float(input("Enter Exam 2 score: "))
exam3 = float(input("Enter Exam 3 score: "))

# Calculate the average score
average = (exam1 + exam2 + exam3) / 3

# Determine the letter grade based on the CS 1300 syllabus scale
if average >= 90:
    grade = "A"
elif average >= 87:
    grade = "A-"
elif average >= 83:
    grade = "B+"
elif average >= 80:
    grade = "B"
elif average >= 77:
    grade = "B-"
elif average >= 73:
    grade = "C+"
elif average >= 70:
    grade = "C"
elif average >= 67:
    grade = "C-"
elif average >= 63:
    grade = "D+"
elif average >= 60:
    grade = "D"
else:
    grade = "F"

# Determine academic standing
if average >= 90:
    status = "Dean's List"
elif average >= 70:
    status = "Good Standing"
elif average >= 60:
    status = "Academic Probation"
else:
    status = "Academic Suspension Warning"

# Print the formatted grade report
print("============================")
print("STUDENT GRADE REPORT")
print("============================")
print("Student:", name)
print("Exam 1:", int(exam1))
print("Exam 2:", int(exam2))
print("Exam 3:", int(exam3))
print("----------------------------")
print(f"Average: {average:.2f}")
print("Grade:", grade)
print("Status:", status)
print("============================")