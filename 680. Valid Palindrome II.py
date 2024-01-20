#这个答案用two pointer做的，这是我第一次接触two pointer
def validPalindrome(s):
    # Time: O(n)
    # Space: O(n)
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            one, two = s[left:right], s[left + 1:right + 1]
            return one == one[::-1] or two == two[::-1]
        left, right = left + 1, right - 1
    return True
result = validPalindrome('abcababa')
print(result)
