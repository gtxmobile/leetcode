class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key= lambda x:x[0])
        if len(intervals)==0 :
            return []
        ans = [intervals[0]]
        for i,t in enumerate(intervals[1:]):
            if t[1]<ans[-1][1]:
                continue
            if t[0] > ans[-1][1]:
                ans.append(t)
            else:
                ans[-1][1]=t[1]
        return ans
