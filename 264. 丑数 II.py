class Solution264:
    def nthUglyNumber(self, n: int) -> int:
        cs = [0, 0, 0]
        arr = [1]
        for i in range(1, n):
            a = arr[cs[0]] * 2
            b = arr[cs[1]] * 3
            c = arr[cs[2]] * 5
            ans = min(a, b, c)
            arr.append(ans)
            if a == ans:
                cs[0] += 1
            if b == ans:
                cs[1] += 1
            if c == ans:
                cs[2] += 1
        return arr[-1]


print(Solution264().nthUglyNumber(10))
print(Solution264().nthUglyNumber(1))

