def print_formatted(number):
    space = len(bin(number)[2:])
    
    for i in range(1,number+1):
        # Decimal
        print(str(i).rjust(space," "),end=" ")
        # Octal
        o = str(oct(i))[2:]
        print(o.rjust(space," "),end=" ")
        # Capitalized Hexadecimal
        h = str(hex(i))[2:]
        h = h.upper()
        print(h.rjust(space," "),end=" ")
        # Binary
        b = str(bin(i))[2:]
        print(b.rjust(space," "))
        
        
        

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
