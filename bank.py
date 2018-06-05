class customers:
	name='GVK'
	balance=200000
	def details(self):
		print("Name",self.name,"Balance",self.balance)
class manager:
	name='Vamsi'     	
	def queries(self):
		print("My name is",self.name)
		print("What is the purpose of your presence \n 1.Inquiry \n 2.Deposit \n 3.Withdrawl")
class actions(customers,manager):
	def deposit(self):
		a=int(input("Tell me the amount u want to deposit"))
		self.balance=self.balance+a
		print("Your Balance is",self.balance)
	def withdraw(self):
		y=int(input("Tell me the amount u want to withdraw"))
		self.balance=self.balance-y
		print("Your Balance is",self.balance)

print("The manager u met is")
l=manager()
z=actions()
l.queries()
n=input('Tell u r choice')
while(True):
	if n==1:
		z.details()
	elif n==2:	
		z.deposit()
	elif n==3:			
		z.withdraw()
	else:
		break
