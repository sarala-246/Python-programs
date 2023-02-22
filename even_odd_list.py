def evenodd(x):
    even=[]
    odd=[]
    for i in x:
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
    return even,odd
x=[3,25,10,14,2,8,17,5]
#print(evenodd(x))
