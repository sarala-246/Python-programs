def palindrome(n):
    if n<0:
        return "negative numbers"

    temp=n
    rev=0
    while(n>0):
        digit=n%10
        rev=rev*10+digit
        n=n//10
        if(temp==rev):
            return "the number is palindrome"
            break
    else:
        return "the number is not palindrome"
print(palindrome(121))
