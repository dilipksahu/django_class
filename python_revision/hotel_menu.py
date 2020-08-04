import os

class Hotel:
    
    def __init__(self,last_bill):
        self.last_bill = last_bill
        print("Wecome! to our Hotel")

    def veg(self):
        print("Item no.   \t 	Dishes	\t\t 	Price")
        print("1)   \t 		Malai Kofta	\t 	Rs.100")
        print("2)   \t 		Palak Paneer	\t 	Rs.150")
        print("0 - Back")
        c=int(input('Select Item Number for purchase=>'))
        self.price = 0
        if c == 1:
            self.price = 100
        elif c== 2:
            self.price = 150
        elif c== 0:
            self.menu()
        else:
            print('Invalid Choice.....!')
            return
        self.add_items(self.price)

    def nveg(self):
        print("Item no.   \t 	Dishes	\t\t 	Price")
        print("1)   \t 		Butter Chicken	\t 	Rs.200")
        print("2)   \t 		Chicken Biryani	\t 	Rs.150")
        c=int(input('Select Item Number for purchase=>'))
        self.price = 0
        if c == 1:
            self.price = 200
        elif c== 2:
            self.price = 150
        elif c== 0:
            self.menu()
        else:
            print('Invalid Choice.....!')
            return
        self.add_items(self.price)
        

    def add_items(self,price):
        self.price == int(price)
        qty=int(input('Enter your quatity=>'))
        amt=qty * self.price
        Total=self.last_bill+amt
        
        ch=input('Do you want to add-on your purchase Y/N=>')
        ch = ch.lower()
        if ch=='y':
            self.last_bill += amt
            self.menu()
        elif ch=='n':
            print('**********************Bill Summary*************************')
            print('Last purchase amount       =                     {}'.format(self.last_bill))
            print('Current Purchase amount    =                     {}'.format(amt))
            print('Total bill amount          =                     {}'.format(Total))
            print('***********************************************************')
            print('Thankyou and Have a Nice Day')
            os._exit(0)
        else:
            print("Invalid Choice.Try agin...!")
            self.menu()
        
        


    def menu(self):
        print(" 1 - Vegitarian Dish")
        print(" 2 - Non-Vegitarian Dish")
        print(" 0 - Exit")
        c = int(input('Select Menu Item Number =>'))
        if c == 0:
            print('Thankyou and Have a Nice Day')
            os._exit(0)
        elif c == 1:
            self.veg()
        elif c == 2:
            self.nveg()
        else:
            print("Invalid Choice.Try agin...!")
            return
            
        
        
    def __del__(self):
        print("******Thankyou visiting us*************")


def main():
    s = Hotel(0)
    s.menu()

main()