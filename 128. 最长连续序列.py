def longestConsecutive(num):
    dic = {}
    longest = 0
    for i in num:
        dic[i] = 1
    for i in num:
        tmp = 1
        qian = i - 1
        hou = i + 1
        while dic.get(qian) == 1:
            dic[qian] += 1
            tmp += 1
            qian -= 1

        while dic.get(hou) == 1:
            dic[hou] += 1
            tmp += 1
            hou += 1
        if tmp > longest:
            longest = tmp
    return longest
