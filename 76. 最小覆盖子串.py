
class Solution76:
    def minWindow(self, s: str, t: str) -> str:
        left = 0
        ans = ""
        td = {}
        l= len(t)
        minl =len(s)+1
        for tc in t:
            td[tc] = td.get(tc,0)+1
        for r,c in enumerate(s):
            if td.get(c) is not None:
                if td[c]>0:
                    l-=1
                td[c]-=1
                while l==0:
                    tmp = td.get(s[left])
                    if tmp is None:
                        left +=1
                        continue
                    td[s[left]]+=1
                    if tmp==0:
                        if r-left+1<minl:
                            ans = s[left:r+1]
                            minl = r-left+1
                        l+=1
                    left+=1
        return ans

print(Solution76().minWindow( s ="ADOBECODEBANC", t = "ABC"))