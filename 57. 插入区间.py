# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """

        ret = []
        merge_val = Interval()

        def merge(inter):
            if not ret or inter.start > ret[-1].end:
                ret.append(inter)
            else:
                ret[-1].end = max(inter.end, ret[-1].end)

        insert = False
        for val in intervals:
            if val.start < newInterval.start:
                merge(val)
            else:
                insert = True
                merge(newInterval)
                merge(val)

        if not insert:
            merge(newInterval)

        return ret
