def fibonacci(n):
    if n<=1:
        return n
    else:
        return (fibonacci(n-1)+fibonacci(n-2))
n=int(input("enter a number:"))
if(n<0):
    print("enter a positive number.")
else:
    print("fibonacci series:")
    for i in range(n):
        print(fibonacci(i))
        
