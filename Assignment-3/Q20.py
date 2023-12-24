# List of original prices
prices = [4.95, 9.95, 14.95, 19.95, 24.95]

# Discount percentage
discount_percentage = 60  # 60% off

# Display the table header
print("Original Price  |  Discount Amount    |  New Price")
print("--------------------------------------------------")

# Loop through each price
for price in prices:
    # Calculate the discount amount
    discount = price * (discount_percentage / 100)
    
    # Calculate the new price after the discount
    new_price = price - discount
    
    # Display the information for each price, rounded to 2 decimal places
    print(f"${price:9.2f}      |  ${discount:15.2f}   |  ${new_price:8.2f}")

