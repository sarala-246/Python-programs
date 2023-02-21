def armstrong(num):
    sum=0
    order=len(str(num))
    temp=num
    while temp>0:
        digit=temp%10
        sum=sum+digit**order
        temp=temp//10
        if num==sum:
            return "number is armstrong"
            break
    else:
        return "not armstrong"
print(armstrong(153))
