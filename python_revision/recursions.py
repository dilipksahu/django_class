
class A:

    def __init__(s,name):
        print("Developer  ",name)
        
    def xyz(s):
        print("Hii")

class B(A):
    
    def __init__(s,name):
        super().__init__(name)
        print("Coder")
    
    def xyz(s):
        print("Hello")
        super().xyz()
       
d=B("Rajesh")
d.xyz()