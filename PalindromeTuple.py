r = (1,3,3,4,4,3,2,1)
def palindrome(t):
    if t == t[::-1]:
        return "Is a palindrome"
    else:
        return "Isn't a palindrome"
print(palindrome(r))