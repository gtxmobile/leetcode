def isPalindrome(x):
    cnt = 1

    if x < 0:
        return False;
    x = abs(x)
    while x / cnt >= 10:
        cnt *= 10
    while x > 0:
        if x % 10 != x / cnt:
            return False
        x = x % cnt / 10
        cnt /= 100
    return True


print(isPalindrome(2147483647))
