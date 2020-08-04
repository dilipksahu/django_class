#object __str__
# class A:

    
#     def xyz(s):
#         print("Hii")


# class B(A):
    
    
#     def abc(s):
#         print("Hello")

       
# d=B()
# d.xyz()
# d.abc()
# print(d)


# ------------------------------------------------------------------------------

#object __str__
class A:

    
    def xyz(s):
        print("Hii")

    def __str__(s):
       return "Thane"

class B(A):
    
    
    def abc(s):
        print("Hello")

    def __str__(s):
        return "Kalyan"
       
d=B()
d.xyz()
d.abc()
print(d)