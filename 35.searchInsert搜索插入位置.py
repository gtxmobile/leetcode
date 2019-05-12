class Solution:
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer
    def searchInsert(self, A, target):
            low=0
            high=len(A)-1
            while low<=high:
                mid=(high+low)/2
                if A[mid]==target:
                    return mid
                elif A[mid]>target:
                    high=mid-1
                else:
                    low=mid+1
            return low

ar=[([1,3,5,6], 5),
([1,3,5,6], 2),
([1,3,5,6], 7),
([1,3,5,6], 0)]

for t,i in ar:
    print Solution().searchInsert(t,i)
