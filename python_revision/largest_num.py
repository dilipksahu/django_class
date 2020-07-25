
num_list = []

while True:
	
	print("1 - Enter number")
	print("0 - Exit")
	c = int(input("Enter your choice:"))
	if c == 1:
		num = int(input("Enter a Numbers "))
		num_list.append(num)
	elif c == 0:
		print("Exiting....!")
		break
	else:
		print("Invalid Choice.Try again")
		continue
num_list.sort() 
print("Largest element is:", num_list[-1]) 	
		



