# FizzBuzz
for i in range(1, 31):

    # If divisible by both 3 and 5
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")

    # If divisible by 3
    elif i % 3 == 0:
        print("Fizz")

    # If divisible by 5
    elif i % 5 == 0:
        print("Buzz")

    # Otherwise print the number
    else:
        print(i)



# Times Table Pattern Program
n = 6

# Loop through rows
for i in range(1, n + 1):
    
    # Loop through columns
    for j in range(1, n + 1):
        
        # Print each value with fixed width (4 spaces) so columns align
        print(f"{i * j:4}", end="")
    
    # Move to the next line after each row
    print()



# Remove duplicates while preserving order
def unique_preserve_order(lst):
    # List to keep track of seen elements
    seen = []
    
    # List to store the result
    result = []
    
    # Loop through each item in the input list
    for item in lst:
        # If item has not been seen before, add it
        if item not in seen:
            seen.append(item)     # Track it as seen
            result.append(item)   # Add to result
    
    # Return the new list with unique elements
    return result

sample_list = [1, 2, 2, 3, 4, 3, 5, 1]
print(unique_preserve_order(sample_list))


# Fibonacci Sequence Genorator
def fibonacci(n):
    # Handle edge cases
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    # Start the sequence with the first two numbers
    fib_list = [0, 1]
    
    # Generate the rest of the sequence
    for i in range(2, n):
        # Each number is the sum of the previous two
        next_value = fib_list[i - 1] + fib_list[i - 2]
        fib_list.append(next_value)
    
    return fib_list

print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(7))
print(fibonacci(10))
print(fibonacci(0))


# Mini Banking System 

# Starting balance
balance = 1000.0

# List to store transaction history
history = []

# Main loop
while True:
    # Display menu
    print("\n--- Banking Menu ---")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Show Transaction History")
    print("5. Quit")
    
    choice = input("Select an option (1-5): ")
    
    # Check Balance
    if choice == "1":
        print(f"Current balance: ${balance:.2f}")
    
    # Deposit
    elif choice == "2":
        amount = float(input("Enter deposit amount: "))
        
        if amount > 0:
            balance += amount
            history.append(("Deposit", amount))
            print(f"Deposited: ${amount:.2f}")
        else:
            print("Amount must be positive.")
    
    # Withdraw
    elif choice == "3":
        amount = float(input("Enter withdrawal amount: "))
        
        if amount <= 0:
            print("Amount must be positive.")
        elif amount > balance:
            print("Insufficient Funds")
        else:
            balance -= amount
            history.append(("Withdraw", amount))
            print(f"Withdrew: ${amount:.2f}")
    
    # Show Transaction History
    elif choice == "4":
        if not history:
            print("no transactions yet")
        else:
            for i, (action, amount) in enumerate(history, start=1):
                print(f"{i}. {action}: ${amount:.2f}")
    
    # Quit
    elif choice == "5":
        print(f"Final balance: ${balance:.2f}")
        break
    
    # Invalid choice
    else:
        print("Invalid choice, please select 1-5.")