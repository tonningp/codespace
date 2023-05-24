def nfact(n):
    if n == 1 or n == 0:  # Base case
        return 1
    else:       # Recursive case
        return n * nfact(n-1)
 
# Get n from user, print nfact(n)
n = int(input())
print(nfact(n))