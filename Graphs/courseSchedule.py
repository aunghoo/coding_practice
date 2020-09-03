'''
https://leetcode.com/problems/course-schedule/
'''

''' Detecting if there is a cycle in the directed graph, edges are given as pairs
'''
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereq_edges = [[] for i in range(numCourses)]
        for pair in prerequisites:
            prereq_edges[pair[1]].append(pair[0])
        visited = set()
        current_path = set()
        # check cycle for each of the courses
        for i in range(numCourses):
            fine = self.visit(i, current_path, visited, prereq_edges)
            if not fine:
                return False
        return True

    def visit(self, current, current_path, visited, prereq_edges):
        # Means there is a cycle
        if current in current_path:
            return False
        # If not in current path and already visited, no need to check
        if current in visited:
            return True
        visited.add(current)
        current_path.add(current)
        # Visit every single node visitable from current node
        for to_visit in prereq_edges[current]:
            fine = self.visit(to_visit, current_path, visited, prereq_edges)
            # there was a cycle!
            if not fine:
                return False
        current_path.remove(current)
        return True