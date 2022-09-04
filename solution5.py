# Write code for algorithm 5 below
def palindrome(s):
    if len(s) < 2:
        return True
    else:
        if s[0] == s[-1]:
            return palindrome(s[1:-1])
        else:
            return False

print(palindrome("racecar"))
print(palindrome("tacocat"))
print(palindrome("palindrome"))
input("Enter to exit")