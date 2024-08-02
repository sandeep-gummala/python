palindrome
n=int(input("enter a number:"))
temp=0
original=n
while(n>0):
    rem=n%10
    temp=temp*10+rem
    n=n//10
if(original==temp):
    print("palindrom")
else:
    print("not palidrom")
