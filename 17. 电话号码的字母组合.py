class Solution17:
    def letterCombinations(self, digits: str):
        d = {
            "2": ("a", "b", "c"),
            "3": ("d", "e", 'f'),
            "4": ("g", "h", "i"),
            "5": ("j", "k", "l"),
            "6": ("m", "n", "o"),
            "7": ("p", "q", "r", "s"),
            "8": ("t", "u", "v"),
            "9": ("w", "x", "y", "z")
        }
        if not digits:
            return []
        arrs = []
        self.back(d, digits, 0, [], arrs)
        return arrs

    def back(self, d, digits, l, sa, ret):
        if l == len(digits):
            ret.append("".join(sa))
            return
        for j in d[digits[l]]:
            for p in j:
                sa.append(p)
                self.back(d, digits, l + 1, sa, ret)
                sa.pop()

print(Solution().letterCombinations("23"))