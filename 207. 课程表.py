class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        self.p = {}
        self.course = [[0] * numCourses for i in range(numCourses)]
        self.visit = [[0] * numCourses for i in range(numCourses)]

        for pair in prerequisites:
            self.course[pair[0]][pair[1]] = 1
        for i in range(numCourses):
            for j in range(numCourses):
                if self.course[i][j]:
                    ret = self.check([i], j)
                    if not ret:
                        return False
        return True

    def check(self, x, y):
        ret = set()
        if self.visit[x][y]:
            return ret
        self.visit[x][y] = 1
        for z in self.course[y]:
            if self.course[y][z]:
                ret.update(self.check(y, z))
        return ret


print(Solution().canFinish(3, [[1, 0], [1, 2], [0, 1]]))
