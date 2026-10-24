class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        

        preqClass = []

        for i in range(len(prerequisites)):
            a = prerequisites[i]
            preqClass.append(a[1])
        
        course = [x for x in range(numCourses)]

        preqClass.sort()
        course.sort()

        if preqClass == course:
            return False

        visited = set()

        graph = {i: [] for i in range(numCourses)}
        needs = [0] * numCourses
        for course, pre in prerequisites:
            graph[pre].append(course)   
            needs[course] += 1
            
        queue = deque()
        for i in range(numCourses):
            if needs[i] == 0:
                queue.append(i)

        taken = 0
        while queue:
            course = queue.popleft()
            taken += 1
            for nxt in graph[course]:
                needs[nxt] -= 1
                if needs[nxt] == 0:
                    queue.append(nxt)

        return taken == numCourses
        
        return True