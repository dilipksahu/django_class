# Write a program to produce Fibonacci series in Python.


def fibo(a):
    f = 0
    s = 1
    if a <= 0:
        print("Required number must be greater than zero.")
    else:
        print(f,s,end=" ")
        for i in range(2,a):
            new = f + s
            print(new,end=" ")
            f = s
            s = new

n = int(input("Enter number of terms needed=>"))
fibo(n)
            
