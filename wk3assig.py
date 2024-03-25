def calculate_discount(price, discount_percent):
  """
  This function calculates the final price after applying a discount.

  Args:
      price: The original price of the item (float).
      discount_percent: The discount percentage (float).

  Returns:
      The final price after applying the discount (float).
  """
  if discount_percent >= 20:
    discount = price * (discount_percent / 100)
    final_price = price - discount
    return final_price
  else:
    return price

# Get user input
original_price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage (e.g., 10 for 10%): "))

# Calculate and display final price
final_price = calculate_discount(original_price, discount_percent)

if discount_percent >= 20:
  print(f"Final price after applying {discount_percent}% discount: ${final_price:.2f}")
else:
  print(f"No discount applied. Price remains: ${original_price:.2f}")
