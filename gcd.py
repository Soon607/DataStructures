def gcd(a,b):
    while a!=0 and b!=0:
        if a>b:
            a-=b
        else:
            b-=a
    return a+b
    
def gcd(a,b):
    while a!=0 and b!=0:
        if a>b:
            a=a%b
        else:
            b=b%a
    return a+b
