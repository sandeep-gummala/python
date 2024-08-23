li=[]
n=int(input("enter no of elements:"))
for i in range(n):
    li.append(int(input("enter element:")))
print(li)
p=int(input("enter a number to remove:"))
if p in li:
    print("before removing:",li)
    li.remove(p)
    print("after removing element:",li)
else:
    print(p,"is not in the list")
