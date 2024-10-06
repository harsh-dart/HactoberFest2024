def calculate_tip(bill_amount, tip_percentage):
    """Calculate the tip based on the bill amount and tip percentage."""
    tip = (bill_amount * tip_percentage) / 100
    total = bill_amount + tip
    return tip, total

def main():
    try:
        # Get input from the user
        bill_amount = float(input("Enter the bill amount: $"))
        tip_percentage = float(input("Enter the tip percentage: %"))
        
        # Calculate tip and total bill
        tip, total = calculate_tip(bill_amount, tip_percentage)
        
        # Display results
        print(f"\nTip Amount: ${tip:.2f}")
        print(f"Total Bill (including tip): ${total:.2f}")
    
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()
