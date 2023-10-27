class Solution67:
    def addBinary(self, a: str, b: str) -> str:
        i,j = len(a),len(b)
        ans = []
        he,c = 0,0
        while i>0 or j >0 or c>0:
            iv = int(a[i-1]) if i>0 else 0
            jv = int(b[j-1]) if j>0 else 0
            he = iv+jv+c
            c = he//2
            ans.append(he - c*2)
            i-=1
            j-=1
        return "".join(map(str,ans[::-1]))