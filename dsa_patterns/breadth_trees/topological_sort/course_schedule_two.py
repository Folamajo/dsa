from collections import deque
def course_schedule_two(num_courses: int, prerequisites : list[list[int]]):
   in_degree = [0] * num_courses
   graph = [[] for _ in range(num_courses)]

   for a, b in prerequisites:
      in_degree[a] += 1
      graph[b].append(a) 

   queue = deque()

   for i in range(num_courses):
      if in_degree[i] == 0: 
         queue.append(i)
   
   order = []

   while queue: 
      course = queue.popleft()
      order.append(course)

      for neighbour in graph[course]:
         in_degree[neighbour] -= 1
         if in_degree[neighbour] == 0:
            queue.append(neighbour)

   if len(order) == num_courses:
      return order
   return [] 


if __name__ == "__main__":
   num_courses = 4
   prerequisites = [[1,0],[2,0],[3,1],[3,2]]
   print(course_schedule_two(4, prerequisites))

   
# In course schedule II we must return a list containing one valid topological order of courses
# so we run the same BFS Kahn algorithm but each time we take a course we just append it to a result list 
# if result list size === num courses we return the list if it is not we return []
# Our ordering is valid because A course is only processed(popped and added to order)
# when its in-degree becomees 0, meaning all its prerequisites have already been taken


# GRaph Construction TIme 
# – Create adjacency list O(n)
# – loop through the prerequisites costs O(m)
# – Total time complexistu of the graph build phase is O(n + m)
# BFS TRAVERSAL TIME
# – Each course is popped at most once –> O(n)
# – Each dependency edge is processed once –> O(m)
# – O(n + m)


# SPACE COMPLEXITY
# The overall space complexity is O(n + m)