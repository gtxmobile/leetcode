class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return an integer
    def search(self, a, key):
        lo = 0
        hi = len(a)
        while lo < hi:
            mid = (lo + hi) // 2
            if a[mid] < key:
                if a[mid] < a[lo] and a[hi - 1] < key:
                    hi = mid
                else:
                    lo = mid + 1
            elif a[mid] > key:
                if a[hi - 1] < a[mid] and a[lo] > key:
                    lo = mid + 1
                else:
                    hi = mid
            else:
                return mid
        return lo if lo != len(a) and a[lo] == key else -1
