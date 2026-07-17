class BankAccount:
    ROI = 10.5

    def __init__(self, AccHoldName, AccountBalance):
        self.AccHoldName = AccHoldName
        self.AccountBalance = AccountBalance
        
    def Display(self):
        print(f"Account Holder Name: {self.AccHoldName},\nCurrent Balance: {self.AccountBalance}")

    def Deposit(self):
        try:
            self.DepositedAmount = float(input("Enter Amount to be Deposited: "))
            #self.amount = float(self.DepositedAmount) 
            if not self.DepositedAmount:
                raise ValueError("No Amount entered")
                print("No deposit made")
            elif self.DepositedAmount <= 0:
                raise ValueError("Deposit amount must be positive.")
            self.AccountBalance = self.AccountBalance + self.DepositedAmount
            return self.AccountBalance
        except ValueError as vobj:
            print("Invalid Input:", vobj)
            return self.AccountBalance
        

    def Withdraw(self):
        try:
            self.WithdrawalAmount = float(input("Enter Withdrawal Amount: "))
            #self.amount = float(self.WithdrawalAmount)
            if not self.WithdrawalAmount:
                raise ValueError("No Amount entered")
            elif self.WithdrawalAmount <= 0:
                raise ValueError("Withdrawal amount must be positive.")  
                print("No withdrawal made")
            elif (self.WithdrawalAmount > self.AccountBalance):
                raise ValueError("Not Sufficient Balance.")
            self.AccountBalance = self.AccountBalance - self.WithdrawalAmount
            return self.AccountBalance
        except ValueError as vobj:
            print("Error:", vobj)
            return self.AccountBalance
    
    def CalculateInterest(self):
        try:
            self.Interest = (self.AccountBalance + BankAccount.ROI) / 100
            return self.Interest
        except Exception as e:
            print("Error calculating interest:", e)
            return 0


obj1 = BankAccount("Nikita Kumbhar", 100000)
obj2 = BankAccount("Anand Patil", 200000)

print("\n--- Object 1 ---")
obj1.Display()
print("Current Balance after Deposited Amount:", obj1.Deposit())
print("Current Balance after Withdrawal Amount:", obj1.Withdraw())
print("Calculate Rate of Interest:", obj1.CalculateInterest())



print("\n--- Object 2 ---")
obj2.Display()
print("Current Balance after Deposited Amount:", obj2.Deposit())
print("Current Balance after Withdrawal Amount:", obj2.Withdraw())
print("Calculate Rate of Interest:", obj2.CalculateInterest())