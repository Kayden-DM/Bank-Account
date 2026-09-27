class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance


    def deposit(self, amount):
        if amount <= 0:
            print("Deposit must be a positive amount.")
            return

        self.balance += amount
        print(f"Deposited ${amount}. New balance is ${self.balance}")


    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal must be a positive amount.")
            return

        if amount > self.balance:
            print(f"You don't have ${amount} to withdraw.")
            return

        self.balance -= amount
        print(f"You have withdrawn ${amount} from your account. Your new balance is ${self.balance}")


    def check_balance(self):
        print(f"Balance for {self.owner}: ${self.balance}")


owner_name = input("Enter account owner's name: ")
account = BankAccount(owner_name)
 
while True:
    print("          BANK ACCOUNT        ")
    print(" 1. Deposit")
    print(" 2. Withdraw")
    print(" 3. Check balance")
    print(" 4. Exit")
 
    choice = input("Choose an option: ")
 
    if choice == "1":
        while True:
            try:
                amount = float(input("Amount to deposit: $"))
                break
            except ValueError:
                print("Please enter a valid number.")
        account.deposit(amount)
 
    elif choice == "2":
        while True:
            try:
                amount = float(input("Amount to withdraw: $"))
                break
            except ValueError:
                print("Please enter a valid number.")
        account.withdraw(amount)
 
    elif choice == "3":
        account.check_balance()
 
    elif choice == "4":
        exit()
 
    else:
        print("Invalid option.")