def fact(n):
    if n<=1:
        return n
    else:
        return n*fact(n-1)
n=int(input("enter a number:"))
if(n<0):
    print("enter a positive number")
else:
    print("factorial of number is:",fact(n)) 
