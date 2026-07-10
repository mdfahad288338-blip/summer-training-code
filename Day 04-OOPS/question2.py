class BankAccount:
    def __init__(self):
        self.accholdername="fahad"
        self.accnumber=111
        self.balance =10000

    
           
    def deposit(self):
        dp = int(input("Enter amount to deposit:"))
        if(dp<1):
            print("invalid amount!")
        else:
            print("New balance:",(self.balance + dp))

    def withdraw(self):
        wd = int(input("Enter amount to withdraw:"))
        if(wd>self.balance):
            print("You dont have this much amount")
        else:
            print("new balance:",(self.balance-wd))

    def display_balance(self):
        print("Balance:",self.balance)

b1 = BankAccount()
b1.display_balance() 
b1.deposit()
b1.withdraw()



