class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        sub=1
        a=[]
        ret = []
        for i in range(1,n):
            sub *=i
            a.append(str(i))
        a.append(str(n))
        cur = k
        k -= 1
        while k >=0 and n>0:
            if k == 0:
                ret.extend(a)
                break
            i = k /sub
            ret.append(a[i])
            a.pop(i)
            k %= sub
            n-=1
            sub /= n

        return "".join(ret)