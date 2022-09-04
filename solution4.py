# Write code for algorithm 4 below
def power(a,b):
    if b <= 1:
        return a
    else:
        return a * power(a, b - 1)

print(power(5,5))
print(power(2,8))
print(power(10,4))

input("Enter to exit")