
'''
def second_max(l):
	s = set(l)
	l=list(s)
	l.sort()
	return l[-2]

print(second_max([78,5,28,45,65,41]))

'''

'''
#OOP's
class A:

    def show(s):
        print("Hiii")

    def display():
       print("Hello")

print("======= Instance Calling=========")
d=A()
d.show()
#d.display() its giving Error
print("=======Class Name=========")      
d=A
d.display()
d.show(12)
print("======= Object Calling=========")
A().show() #object
print("=======ClassName Calling=========")
A.show(12) #class Name

# instance function or constant function
'''

# class A:
      
    # def show(k,a,b):
        # k - instance variable , a,b,c - local variable
        # k.a = a
        # k.b = b
        # c =96
        # k.c =c
        # print(a,b,c)

    # def display(m):
       # print(m.a,m.b,m.c)
       
# s = A()
# s.show(5,6)
# s.display()

# ******************* same as just above ***************
class A:

    def show(self,a,b):
        # k - instance variable , a,b,c - local variable
        self.a = a
        self.b = b
        c =96
        self.c =c
        print(a,b,c)

    def display(self):
       print(self.a,self.b,self.c)
       
s = A()
s.show(5,6)
s.display()
