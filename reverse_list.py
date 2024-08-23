li=[]
n=int(input())
for i in range(n):
    li.append(int(input("enter a number:")))
print(li)
print("reverse of the list is :")
li.reverse()
print(li)
print(li[::-1])
