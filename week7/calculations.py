def calculation(a,b,o):
    return eval(f'{a} {o} {b}')
a=int(input("enter a number:"))
b=int(input("enter second number:"))
o=input("enter the operator:")
print(calculation(a,b,o))
