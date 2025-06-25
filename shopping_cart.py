# Create a shopping cart system that collects food items and their prices
# and prints a summary with the total cost at the end.

# List to store food items
food_list = []

# List to store prices of food items
prices = []

# Infinite loop to allow multiple entries until user exits
while True:
    food = input("Enter food item or press X to exit: ")

    # Exit condition
    if food.lower() == 'x':
        break
    else:
        # Prompt the user to enter price for the item
        try:
            price = float(input(f"Enter the price of the {food}: R"))
            food_list.append(food)       # Add food to the list
            prices.append(price)         # Add price to the list
        except ValueError:
            print("Please enter a valid number for the price.")

# Print the cart contents
print("\n--- YOUR CART ---")
for i in range(len(food_list)):
    print(f"{food_list[i]} - R{prices[i]:.2f}")

# Calculate total price
total_price = 0
for price in prices:
    total_price += price

# Print the total amount
print(f"\nYour total is: R{total_price:.2f}")
