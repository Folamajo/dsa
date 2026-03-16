from collections import deque

def course_schedule(num_courses: int, prerequisites: list[list[int]]) -> bool:

   # Create adjencency list for numCourses
   graph = [[] for _ in range(num_courses)]
   # Implement in degree array
   in_degree = [0] * num_courses

   for a, b in prerequisites:
      graph[b].append(a)
      in_degree[a] += 1
   
   queue = deque()
   for i in range(num_courses):
      if in_degree[i] == 0:
         queue.append(i)
   
   completed = 0

   while queue:
      course = queue.popleft()
      completed += 1

      for neighbour in graph[course]:
         in_degree[neighbour] -= 1  
         if in_degree[neighbour] == 0:
            queue.append(neighbour)

   return completed == num_courses

if __name__ == "__main__":
   num_courses = 2
   prerequisites = [[1,0],[0,1]]
   print(course_schedule(num_courses, prerequisites))
