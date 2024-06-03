class Account:
   def __init__(self,balance,account_no):
       self.balance = balance
       self.account_no = account_no
   def credit(self,amount):
        self.balance += amount
        print(amount,"has been credited to you","total balamce left :-",self.balance)
   def debit(self,amount):
        self.balance -= amount
        print(amount,"has been debited from you","total balamce left :",self.balance)
   def get_balance(self):
        print(self.balance)
        a1 = Account(10000,1234)
a2 = Account(20000,5678)
a1.credit(500)
a2.credit(50650)

a1.debit(200)
a1.get_balance()
a2.get_balance()
