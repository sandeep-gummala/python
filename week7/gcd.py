def gcd(a,b):
    gcd=0
    for i in range(1,min(a,b)+1):
        if(a%i==0 and b%i==0 and gcd<i):
            gcd=i
    return gcd
print(gcd(15,25))
