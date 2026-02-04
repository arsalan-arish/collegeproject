
def is_palindrome(n: int):
    n = str(n)
    reverse = n[::-1]
    if n == reverse:
        return "Palindrome number"
    return "Not a Palindrome Number"

print(is_palindrome(12321))
print(is_palindrome(456))

