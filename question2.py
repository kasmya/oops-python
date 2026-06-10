#create an account class with 2 attributes - balance and account no.
#make methods for debit, credit and printing the balance

class Account():
  def __init__(self,bal,acc):
    self.balance = bal
    self.account_no = acc
    print("total balance is", self.get_balance())

  #debit method
  def debit(self,amount):
    self.balance -= amount
    print("Rs. ", amount, "was debited")
    print("total balance is", self.get_balance())

 #credit method
 def credit(self,amount):
    self.balance += amount
    print("Rs. ", amount, "was credited")
    print("total balance is", self.get_balance())

 def get_balance(self): 
   return self.balance
   
acc1 = Account(10000, 11)
print(acc1.balance)
print(acc1.account_no)

    
