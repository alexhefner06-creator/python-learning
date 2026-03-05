# Get user input
temperature = int(input("Enter the current temperature (°F): "))
raining = input("Is it raining? (yes/no): ").lower()

# Determine the advisory message
if temperature > 100:
    # Temperature above 100 always triggers extreme heat warning
    print("EXTREME HEAT WARNING: Stay indoors!")

elif temperature > 85:
    # Temperature between 86 and 100
    if raining == "yes":
        print("Warm rain — watch for flash floods.")
    else:
        print("Hot and dry — stay hydrated.")

elif temperature >= 60:
    # Temperature between 60 and 85
    if raining == "yes":
        print("Grab an umbrella!")
    else:
        print("Nice weather — enjoy your day!")

elif temperature >= 32:
    # Temperature between 32 and 59
    print("It's cold — bundle up!")

else:
    # Temperature below 32
    print("FREEZE WARNING: Roads may be icy!")