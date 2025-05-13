def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying a discount if the discount is 20% or higher.
    Args:
        price (float): The original price of the item.
        discount_percent (float): The discount percentage to apply.
    Returns:
        float: The final price after discount, or the original price if discount < 20%.
    """
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        return price - discount_amount
    else:
        return price

if __name__ == "__main__":
    try:
        price = float(input("Enter the original price: "))
        discount_percent = float(input("Enter the discount percentage: "))
        final_price = calculate_discount(price, discount_percent)
        if discount_percent >= 20:
            print(f"Final price after {discount_percent}% discount: {final_price:.2f}")
        else:
            print(f"No discount applied. Final price: {final_price:.2f}")
    except ValueError:
        print("Invalid input. Please enter numeric values.")
