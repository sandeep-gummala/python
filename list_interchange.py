li=[]
n=int(input("enter no of elements:"))
for i in range(n):
    li.append(int(input("enter element:")))
print("before iterchanging:")
print(li)
temp=li[-1]
li[-1]=li[0]
li[0]=temp
print("after interchanging:")
print(li)
