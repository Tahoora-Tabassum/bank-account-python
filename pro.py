class BankAccount:
    def __init__(self, account_holder):
       self.account_holder = account_holder 
       self.balance = 0
       
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited Rs. {amount}")
        
    def withdraw(self, amount):
        if (amount <= self.balance):
            self.balance -= amount
            print(f"Withdrawed Rs. {amount}")
        else:
            print("amount is insufficient...")
        
    def display_balance(self):
        print("account holder is: ", self.account_holder)
        print("current balance: ", self.balance)
        
        
a = BankAccount(input("Enter account name: "))
x = int(input("Enter amount to be deposite:"))
a.deposit(x)
y = int(input("Enter amount to withdraw: "))
a.withdraw(y)
a.display_balance()
        
        