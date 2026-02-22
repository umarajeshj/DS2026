class BankAccount:
    def __init__(self,account_holder,account_type,balance):
        self.account_holder = account_holder
        self.balance = balance
        self.account_type = account_type

#deposit amount
    def deposit(self,amount):
        totalAmountAfterDeposit = self.balance + amount
        self.balance = totalAmountAfterDeposit
    
#withdraw amount
    def withdraw(self,amount):
        if(self.balance>amount):
            totalAmountAfterWithdraw = self.balance - amount
            self.balance = totalAmountAfterWithdraw
        else:
            print("**** Insufficient Balance ****")
    
#Print account holder details
    def print_details(self):
        """Displays the current details of the account."""
        print("-" * 30)
        print(f"Account Holder: {self.account_holder}")
        print(f"Account Type: {self.account_type}")
        print(f"Current Balance: ${self.balance:.2f}")
        print("-" * 30)

account1 = BankAccount("Anu","Savings",10000.500)
account2 = BankAccount("John","Current",5000)

if __name__ == "__main__":
    account1.deposit(1000)
    account2.withdraw(6500)
    
print("\n--- Final Account Details ---")
account1.print_details()
account2.print_details()

