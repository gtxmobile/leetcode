def shortestPalindrome(s: str) -> str:
    if len(s) < 2:
        return s
    for i in range(len(s), 0, -1):
        # print(arr)
        if s[:i] == s[i:0:-1]:
            return s[len(s):i:-1] + s
    return s[len(s):0:-1] + s


print(shortestPalindrome("aacecaaa"))
print(shortestPalindrome('abcd'))
print(shortestPalindrome("abbacd"))
