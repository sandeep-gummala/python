li=[]
n=int(input("enter size of elements:"))
for i in range(n):
    li.append(int(input("enter a number:")))
print(li)
print(sum(li))
avg=sum(li)/n
print(avg)
