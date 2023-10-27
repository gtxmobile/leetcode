class Solution91:
    def numDecodings(self, s: str) -> int:
        ls = list(map(int,s))
        if ls[0] == 0:
            return 0
        l = len(ls)
        dp = [0]*(l+1)
        dp[0]=1
        dp[1]=1
        for i in range(1,l):
            if ls[i] == 0:
                if 0<ls[i-1]<3:
                    dp[i+1] = dp[i-1]
                    continue
                else:
                    return 0
            elif ls[i-1] ==1 or (ls[i-1] ==2 and ls[i]<7):
                dp[i+1] = dp[i-1]+dp[i]
            else:
                dp[i+1] = dp[i]
        return dp[-1]
