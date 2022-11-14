from typing import List


class Solution4:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        self.nums1 = nums1
        self.nums2 = nums2
        self.l1 = len(nums1)
        self.l2 = len(nums2)
        l = self.l1 + self.l2
        left = (l + 1) // 2
        right = (l + 2) // 2
        return (self.findKthNum(left, 0, 0) + self.findKthNum(right, 0, 0)) / 2
        # if l & 1 == 1:
        #     return self.findKthNum(l // 2 + 1, 0, 0)
        # else:
        #     return (self.findKthNum(l // 2, 0, 0) + self.findKthNum(l // 2 + 1, 0, 0)) / 2.0

    def getKthElement(self, k, idx1, idx2):
        if idx1 == self.l1:
            return self.nums2[idx2 + k - 1]
        if idx2 == self.l2:
            return self.nums1[idx1 + k - 1]
        if k == 1:
            return min(self.nums1[idx1], self.nums2[idx2])
        mid = k // 2
        new_idx1 = min(idx1 + mid, self.l1) - 1
        new_idx2 = min(idx2 + mid, self.l2) - 1
        if self.nums1[new_idx1] < self.nums2[new_idx2]:
            k -= new_idx1 - idx1 + 1
        else:
            k -= new_idx2 - idx2 + 1

        return self.getKthElement(k-mid, new_idx1 + 1, new_idx2 + 1)

    def findKthNum(self, k, i, j):
        if i >= self.l1:
            return self.nums2[j + k - 1]
        if j >= self.l2:
            return self.nums1[i + k - 1]
        if k == 1:
            return min(self.nums1[i], self.nums2[j])
        mid = k // 2
        if i + mid - 1 < self.l1:
            mid1 = self.nums1[i + mid - 1]
        else:
            mid1 = 1 << 32
        if j + mid - 1 < self.l2:
            mid2 = self.nums2[j + mid - 1]
        else:
            mid2 = 1 << 32
        if mid1 < mid2:
            return self.findKthNum(k - mid, i + mid, j)
        else:
            return self.findKthNum(k - mid, i, j + mid)


print(Solution4().findMedianSortedArrays([1, 3], [2]))
