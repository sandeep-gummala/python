def GCD(a,b):
    if b==0:
        return a
    else:
        return GCD(b,a%b)
a=int(input("enter a value:"))
b=int(input("enter b value:"))

print("GCD of a ad b is:",GCD(a,b))
        
