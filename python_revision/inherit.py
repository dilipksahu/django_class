class D:
    a=30

    def abc(s):
        print("Developer")

class A:
    a=20

    def abc(s):
        print("Hii")

class B(A):
    b=90

    def xyz(s):
        print(s.a+s.b)
        print("Hello")
       
d=B()
d.abc()
d.xyz()
print(d.a+d.b)
