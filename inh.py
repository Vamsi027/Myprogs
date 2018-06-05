class parent:
	def __init__(self,name):
		self.name=name
		
	def disp(self):
		print("Tell me his name again!!",self.name)
class child(parent):
	def __init__(self,age):
		self.age=age
	def dis(self):
		print("Age?",self.age)
y=parent("Thanos")
x=child(40)
y.disp()
x.dis()
