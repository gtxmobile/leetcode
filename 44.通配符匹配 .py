def isMatch(s, p):
    plen = len(p)
    slen = len(s)
    i = 0
    j = 0
    hasxing = False
    while j < slen and i < plen:
        if p[i] is '?':
            i += 1
            j += 1
        elif p[i] == '*':
            hasxing = True
            i += 1
        elif s[j] != p[i]:
            return False
        else:
            i += 1
            j += 1
    if slen > plen:
        if hasxing: return True
        return False
    elif slen == plen:
        return True
    else:
        while i < plen:
            if p[i] != '*':
                return False
            return True
        return False


tests = [("aa", "a"),
         ("aa", "aa"),
         ("aaa", "aa"),
         ("aa", "*"),
         ("aa", "a*"),
         ("ab", "?*"),
         ("aab", "c*a*b")]

for i in tests:
    print
    isMatch(*i)
