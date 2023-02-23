def secondlargest(lst):
    lst.sort()
    return(lst[len(lst)-2])
    

print(secondlargest([10,25,600,509,525]))
