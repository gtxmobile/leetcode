class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        self.course = [[] * numCourses for i in range(numCourses)]
        self.rudu = [0] * numCourses
        queue = []
        for pair in prerequisites:
            self.course[pair[1]].append(pair[0])
            self.rudu[pair[0]] += 1
        for i in range(numCourses):
            if self.rudu[i] == 0:
                queue.append(i)
        ans = []
        cnt = numCourses
        while queue:
            i = queue.pop()
            ans.append(i)
            cnt -=1
            for j in self.course[i]:
                    self.rudu[j] -= 1
                    if self.rudu[j] == 0:
                        queue.append(j)
        if cnt:
            return []
        return ans


print(Solution().findOrder(4, [[1,0],[2,0],[3,1],[3,2]]))
