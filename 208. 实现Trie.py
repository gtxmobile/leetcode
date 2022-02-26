class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        self.course = [[0] * numCourses for i in range(numCourses)]
        self.rudu = [0] * numCourses
        queue = []
        for pair in prerequisites:
            self.course[pair[0]][pair[1]] = 1
            self.rudu[pair[1]] += 1
        for i in range(numCourses):
            if self.rudu[i] == 0:
                queue.append(i)
        cnt = numCourses
        while queue:
            i = queue.pop()
            cnt -= 1
            for j in range(numCourses):
                if self.course[i][j]:
                    self.rudu[j] -= 1
                    if self.rudu[j] == 0:
                        queue.append(j)
        return cnt == 0


print(Solution().canFinish(3, [[1, 0], [1, 2], [0, 1]]))
