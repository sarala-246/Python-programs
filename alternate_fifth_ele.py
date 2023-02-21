def alter(n):
    n1=[]
    for i in range(1,n+1):
        n1.append(i)
        n2=n1[4::5]

    return n2
print(alter(100))


