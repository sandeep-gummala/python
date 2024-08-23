li=[]
n=int(input("enter no of elements:"))
for i in range(n):
    li.append(int(input("enter element:")))
print(li)
even=[]
odd=[]
for i in li:
    if(i%2==0):
        even.append(i)
    else:
        odd.append(i)
print("even numbers of list:",even)
print("odd numbers of list:",odd)
