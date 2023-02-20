
def prime(n):
    if n==1:
        return "neither prime nor composite"
    if n<0 or n==0:
        return "zero"
    for i in range(2,n):
        if(n%i)==0:
            return "it is not prime"
        else:
            return "yes it is prime"
 