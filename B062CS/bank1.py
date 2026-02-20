class BankAccount:
    # Class Attributes
    bank_name = "National Bank"
    total_accounts = 0
    total_bank_balance = 0

    def __init__(self, account_holder, initial_deposit):
        self.account_holder = account_holder
        self.balance = initial_deposit

        BankAccount.total_accounts += 1
        BankAccount.total_bank_balance += initial_deposit

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            BankAccount.total_bank_balance += amount
            print("Deposit successful!")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount.")
        elif amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            BankAccount.total_bank_balance -= amount
            print("Withdrawal successful!")

    def display_account_info(self):
        print("\n--- Account Information ---")
        print(f"Bank Name: {BankAccount.bank_name}")
        print(f"Account Holder: {self.account_holder}")
        print(f"Balance: {self.balance}")
        print("----------------------------\n")


def main():
    accounts = {}

    while True:
        print("====== Bank Management System ======")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Display Account Info")
        print("5. Display Bank Summary")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter account holder name: ")
            initial_deposit = float(input("Enter initial deposit: "))
            account = BankAccount(name, initial_deposit)
            accounts[name] = account
            print("Account created successfully!\n")

        elif choice == "2":
            name = input("Enter account holder name: ")
            if name in accounts:
                amount = float(input("Enter deposit amount: "))
                accounts[name].deposit(amount)
            else:
                print("Account not found!")

        elif choice == "3":
            name = input("Enter account holder name: ")
            if name in accounts:
                amount = float(input("Enter withdrawal amount: "))
                accounts[name].withdraw(amount)
            else:
                print("Account not found!")

        elif choice == "4":
            name = input("Enter account holder name: ")
            if name in accounts:
                accounts[name].display_account_info()
            else:
                print("Account not found!")

        elif choice == "5":
            print("\n--- Bank Summary ---")
            print(f"Bank Name: {BankAccount.bank_name}")
            print(f"Total Accounts: {BankAccount.total_accounts}")
            print(f"Total Bank Balance: {BankAccount.total_bank_balance}")
            print("---------------------\n")

        elif choice == "6":
            print("Exiting program...")
            break

        else:
            print("Invalid choice! Please try again.\n")


if __name__ == "__main__":
    main()