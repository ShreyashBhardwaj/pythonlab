class ATM:
    def __init__(self, pin, balance=0):
        self.__pin = pin  # Private attribute for PIN
        self.__balance = balance  # Private attribute for balance

    # Function to verify the entered PIN
    def verify_pin(self, pin):
        return self.__pin == pin

    # Function to check balance
    def check_balance(self):
        return self.__balance

    # Function to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"₹{amount} deposited successfully.")
        else:
            print("Invalid deposit amount.")

    # Function to withdraw money
    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient balance.")
        elif amount <= 0:
            print("Invalid withdrawal amount.")
        else:
            self.__balance -= amount
            print(f"₹{amount} withdrawn successfully.")


# Main Program
def main():
    # Read PIN and initial balance from the user
    user_pin = int(input("Set your ATM PIN: "))
    initial_balance = float(input("Set your initial balance (₹): "))

    # Initialize ATM object with user-provided PIN and balance
    atm = ATM(pin=user_pin, balance=initial_balance)

    print("\nWelcome to the ATM!")
    entered_pin = int(input("Enter your PIN: "))

    # Verify PIN
    if not atm.verify_pin(entered_pin):
        print("Incorrect PIN. Access denied.")
        return

    while True:
        print("\nChoose an option:")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            # Check balance
            print(f"Your current balance is: ₹{atm.check_balance()}")
        elif choice == 2:
            # Deposit money
            amount = float(input("Enter the amount to deposit: ₹"))
            atm.deposit(amount)
        elif choice == 3:
            # Withdraw money
            amount = float(input("Enter the amount to withdraw: ₹"))
            atm.withdraw(amount)
        elif choice == 4:
            # Exit
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
main()
