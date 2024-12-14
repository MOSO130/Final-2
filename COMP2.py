def savings_calculator():
    try:
        # Get the user's paycheck amount
        paycheck = float(input("Enter your paycheck amount: "))

        if paycheck <= 0:
            print("Paycheck amount should be greater than 0.")
            return

        # Get the percentage the user wants to save
        percentage = float(input("Enter the percentage of your paycheck you want to save (e.g., 20 for 20%): "))

        if percentage < 0 or percentage > 100:
            print("Please enter a valid percentage between 0 and 100.")
            return

        # Calculate the amount to save
        amount_to_save = (percentage / 100) * paycheck

        print(f"You should save ${amount_to_save:.2f} from your paycheck of ${paycheck:.2f}.")

    except ValueError:
        print("Invalid input. Please enter numeric values.")


if __name__ == "__main__":
    savings_calculator()
