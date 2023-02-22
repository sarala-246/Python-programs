def factorial(n):
    if n<0:
        return 0
    elif (n==0 or n==1):
        return 1
    res=1
    for i in range(1,n+1):
        res = res * i
    return res
print(factorial(5))
