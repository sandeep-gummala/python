li=[]
n=int(input("enter no of elements:"))
for i in range(n):
    li.append(int(input("enter element:")))
print(li)
print("position of maximum number of list=",li.index(max(li)))
print("position of minimum number of list=",li.index(min(li)))
