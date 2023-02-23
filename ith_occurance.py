def ithoccurance(l):
    count=0
    b=int(input("enter the occurance: "))
    c=str(input("enter the word to be removed:"))
    for i in range(0,len(l)+1):
        if l[i]==c:
            count+=1
            if count==b:
                del l[i]
                break
    return l
l=['hi','hello','python','hi','hello','hi']
#print(ithoccurance(l))
