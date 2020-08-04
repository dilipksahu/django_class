# class Emp:


#     def getInfo(self):
#         self.name = input("Employee Name:")
#         self.contact  = int(input("Contact Number:"))
#         self.workexp = int(input("Total Work Experience in Years:"))
#         self.companyname = input("Company Name:")
#         self.salary = float(input("Salary:"))


#     def totalSalary(self):
#         self.netsal = self.salary + self.bonus - self.pf

#     def pf(self):
#         self.pf = self.salary * 0.12

#     def bonus(self):
#         if self.workexp > 20:
#             self.bonus = self.salary * 0.15
#         elif self.workexp > 10:
#             self.bonus = self.salary * 0.10
#         elif self.workexp > 5:
#             self.bonus = self.salary * 0.05
#         else:
#             self.bonus = 0
            

#     def displayInfo(self):
#         print("**********Displaying Employee Payslip*************")
#         print("Employee Name:",self.name)
#         print("Contact Number:",self.contact)
#         print("Work Experience:",self.workexp)
#         print("Company Nmae:",self.companyname)
#         print("salary:",self.salary)
#         print("Bonus Allowcated:",self.bonus)
#         print("PF Deducted:",self.pf)
#         print("Total Net Salary:",self.netsal)

# def main():
#     e = Emp()
#     e.getInfo()
#     e.bonus()
#     e.pf()
#     e.totalSalary()
#     e.displayInfo()
    

# #if __name__=='___main__':
# main()

#--------------------------------------------------------------------------------------

class Emp:
    def __init__(s,name,contact,workExp,salary,cname):
        s.name=name
        s.contact=contact
        s.workExp=workExp
        s.salary=salary
        s.cname=cname

    def totalSalary(s):
        return s.salary*12*s.workExp

    def pf(s):
        return s.totalSalary()*0.12

    def bonus(s):
        if s.workExp>5:
            return 10000
        else:
            return 5000
    def __str__(s):
        t=(s.name,s.contact,s.workExp,s.salary,s.cname,s.totalSalary(),s.pf(),s.bonus())
        return str(t)

e=Emp("Aditi",88996655,5,80000,'ITV')
print(e)