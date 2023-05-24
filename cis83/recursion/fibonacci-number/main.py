"""
F(0) = 1
F(1) = 1
F(2) = 2
F(3) = 3
F(4) = 5
F(5) = 8
F(6) = 13 
F(7) = 21
F(n) = F(n-2) + F(n-1)
"""
def compute_nth_fib(num):
    if num == 1 or num == 0:
        return 1
    else:
        return compute_nth_fib(num-1) + compute_nth_fib(num-2)

for i in range(25):
    #print(compute_nth_fib(int(input())))
    print(compute_nth_fib(i))