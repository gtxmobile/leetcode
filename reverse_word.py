def reverseWords(s):
    words=s.split(' ')
    words=[w for w in words if w]
    return ' '.join(words[::-1])
#print reverseWords("1 ")


