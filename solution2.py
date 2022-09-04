# Write code for algorithm 2 below
def count_to(n, x=0):
    if x > n:
        return
    else:
        print(x)
        count_to(n, x + 1)

count_to(20)
input("Enter to exit")