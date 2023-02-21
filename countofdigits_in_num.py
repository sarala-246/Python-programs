
def digitcount(n):
    if n<0:
        return "cant count negative numbers"
    if n==0:
        return 0

    count=0
    while n!=0:
        n=n//10
        count=count+1
    return count
print(digitcount(452356))
