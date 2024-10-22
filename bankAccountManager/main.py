# A program that manages your bank account, allows you to create accounts, add and remove from accounts, and check their balance

#comments added by Alec George

class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount): #add money to your account, asks for the account number and how much to add
        if amount > 0: #check if you actually added money
            self.balance += amount
            return True
        return False

    def withdraw(self, amount): #remove money from your account, asks for the account number and how much to remove
        if 0 < amount <= self.balance: #check if you're actually removing money, and won't let you remove more money than is in your account
            self.balance -= amount
            return True
        return False

    def get_balance(self): #shows how much money is currently in an account
        return self.balance

def create_account(): #creates a new account
    account_number = input("Enter account number: ") #user input for the number of the account
    initial_balance = float(input("Enter initial balance: ")) #user input for the starting balance of the account
    return BankAccount(account_number, initial_balance)

def main():
    accounts = {}
    while True: #keep repeating until the user wants to stop
        # options for user input, they type a number depending on what they want to do
        print("\n1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1': # if user typed 1, create a new account
            account = create_account()
            accounts[account.account_number] = account
            print(f"Account {account.account_number} created successfully!")
        
        elif choice in ['2', '3', '4']: # if user typed 2, 3, or 4, ask for their account number
            account_number = input("Enter account number: ")
            if account_number in accounts: #only continue if account with the number the user inputted exists
                account = accounts[account_number]
                if choice == '2': #if user typed 2, add money to account
                    amount = float(input("Enter deposit amount: "))
                    if account.deposit(amount): #only deposit if the user entered a valid amount (number greater than 0)
                        print(f"Deposited ${amount:.2f} successfully!")
                    else:
                        print("Invalid deposit amount.")
                elif choice == '3': #if user typed 3, remove money from account
                    amount = float(input("Enter withdrawal amount: "))
                    if account.withdraw(amount): #only remove if the user entered a valid amount (number greater than 0 and less than the amount of money in the account)
                        print(f"Withdrawn ${amount:.2f} successfully!")
                    else:
                        print("Invalid withdrawal amount or insufficient funds.")
                else: #if user typed 4, show how much money is in the account
                    print(f"Current balance: ${account.get_balance():.2f}")
            else:
                print("Account not found.")
        
        elif choice == '5': #if user typed 5, stop running program
            print("Thank you for using our banking system. Goodbye!")
            break
        
        else: #if the user didn't type a valid number, do nothing
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()