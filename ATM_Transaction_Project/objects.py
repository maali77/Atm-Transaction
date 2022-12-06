from dataclasses import dataclass
@dataclass
class Atm:
    #balance:float = 0.0
    #previousTransaction:float = 0.0
    #customerName:str = ""
    #customerId:str =  ""

    def __init__(self,customerName,customerId):
        self.customerName  = customerName
        self.customerId = customerId
        self.balance = 0
        self.previousTransaction = 0

    def deposit(self,amount):
        if amount != 0:
            self.balance = self.balance+amount
            self.previousTransaction = amount

    def withdraw(self,amount):
        if amount != 0:
            self.balance = self.balance - amount
            self.previousTransaction = -amount

    def getPreviousTransaction(self):
        if self.previousTransaction > 0:
            print("deposited: ", self.previousTransaction)
        elif self.previousTransaction < 0:
            print("Withdrawn: ", abs(self.previousTransaction))
        else:
            print("No transaction has taken place")
            
    def calculateInterest(self,years):
        interestRate = .033
        newBalance = (self.balance * interestRate  * years) + self.balance
        print("The current interest rate is ", (100*interestRate),"%")
        print("After",years,"years, your new balance will be:",newBalance)
        
    
    def showMenu(self):
        print("Welcome, ", self.customerName, "!")
        print("Your ID is: ", self.customerId)
        print()
        print("What would you like to do?")
        print()
        print("A. Check your current balance?")
        print("B. Make a deposit?")
        print("C. Make a withdrawl")
        print("D. View previous transaction")
        print("E. Calculate Interest")
        print("F. Exit")
        
        while True:
            option = input("Please enter an option: ")
            print()
            if option == 'A' or option == 'a':
                print("===============================")
                print("Balance = $",self.balance)
                print("===============================")
                print()
                continue
            elif option == 'B' or option == 'b':
                amount = float(input("Enter an amount to deposit:"))
                Atm.deposit(self,amount)
                print()
                continue
            elif option == 'C' or option == 'c':
                amount = float(input("Enter an amount to withdraw:"))
                Atm.withdraw(self,amount)
                print()
                continue
            elif option == 'D' or option == 'd':
                print("==============================")
                Atm.getPreviousTransaction(self)
                print("==============================")
                print()
                continue
            elif option == 'E' or option == 'e':
                years = int(input("Enter how many years of accrued interest: "))
                Atm.calculateInterest(self,years)
                continue
            elif option == 'F' or option == 'f':
                print("==============================")
                break
            else:
                print("Error invalid option. Please enter A, B, C, D, or E to access ATM.")
                break


                      
    
    
      
            
        
        
    
