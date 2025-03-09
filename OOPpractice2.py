class Account():

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    
    def deposit(self,amount):
        self.balance = self.balance + amount
        print (f"Your new balance is {self.balance}")
    
    def withdrawl(self, amount):
        if self.balance >= amount:
            self.balance = self.balance - amount
            print (f"Your new balance is {self.balance}")  
        else:
            print (f"you do not have enough savings to withdraw {self.amount}")
        
        

acct1 = Account('Ashley',100)
print(acct1.owner)
print(acct1.balance)
print(acct1.withdrawl(200))