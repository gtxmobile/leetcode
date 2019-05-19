class Solution:
    # @param A a list of integers
    # @param target an integer
    # @return a boolean
    def search(self, a, key):
        lo = 0
        hi = len(a)
        while lo < hi:
            mid = (lo + hi) // 2
            if a[mid] < key:
                if a[mid] < a[lo] and a[hi-1] < key:
                    hi = mid
                else:
                    if a[mid]==a[lo]:
                        lo+=1
                    else:
                        lo = mid+1
            elif a[mid]>key:
                if a[hi-1] < a[mid] and key < a[lo]:
                    lo = mid+1
                else:
                    if a[hi-1]==a[mid]:
                        hi-=1
                    else:
                        hi = mid
            else:
                return True
        return False