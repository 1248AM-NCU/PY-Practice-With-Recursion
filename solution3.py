# Write code for algorithm 3 below
def fib(n,a=0,b=1):
    if n <= 1:
        print(a)
    else:
        return fib(n - 1, b, a + b)


fib(2)
fib(4)
fib(8)
fib(16)

input("Enter to exit")