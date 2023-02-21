def average(lst):
    sum=0
    for i in lst:
        sum=sum+i
    avg=sum/(len(lst))
    return avg
#print(average([10,20,30,40,50]))
