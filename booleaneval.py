# Ask the user for three integer values
a = int(input("Enter value for a: "))
b = int(input("Enter value for b: "))
c = int(input("Enter value for c: "))

# Evaluate a chained comparison
expr1 = a < b < c

# Evaluate a logical expression using De Morgan's Law
expr2 = not (a > b or b > c)

# Evaluate an equivalent expression written differently
expr3 = a <= b and b <= c

# Print the results of each expression
print("a < b < c:", expr1)
print("not (a > b or b > c):", expr2)
print("a <= b and b <= c:", expr3)

# Check whether the second and third expressions give the same result
print("Expressions 2 and 3 produce the same result:", expr2 == expr3)