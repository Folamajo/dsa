from collections import deque

def course_schedule(num_courses: int, prerequisites: list[list[int]]) -> bool:

   # Create adjencency list for numCourses
   # The graph represents which prerequisites unlock which course, the index are the prerequisites
   graph = [[] for _ in range(num_courses)]
   # Implement in degree array
   in_degree = [0] * num_courses

   for a, b in prerequisites:
      graph[b].append(a)
      in_degree[a] += 1
   
   # Get the first course that  can be taken
   queue = deque()
   for i in range(num_courses):
      if in_degree[i] == 0:
         queue.append(i)
   
   courses_completed = 0

   while queue:
      course = queue.popleft()
      courses_completed += 1

      for neighbour in graph[course]:
         in_degree[neighbour] -= 1  
         if in_degree[neighbour] == 0:
            queue.append(neighbour)

   return courses_completed == num_courses

if __name__ == "__main__":
   num_courses = 2
   prerequisites = [[1,0],[0,1]]
   print(course_schedule(num_courses, prerequisites))


# The graph is set set up in a way that each index represents the prerequisite and the value represents the courses that becomes closer to being unlocked
# In the in_degree : the index represents the course and the value represents how many courses are needed for that course to be unlocked. 
# So when a value is 0 we know that course is ready because it has no prerequisites it can be added to the queue 

# We use a deque (double ended queue) that allows us to add and remove data efficiently from both the left and right and side. in O(1)
# A deque (double-ended queue) is a linear data structure in which data can be inserted and removed from both ends — the front and the rear. 
# This makes it more flexible than a normal queue (which allows insertion only at the rear and deletion only at the front). 
# In a deque, elements can enter either by inserting at the front (push_front) or inserting at the rear (push_back), and they can leave either by removing from the front (pop_front) or removing from the rear (pop_back). 
# Because of this two-way access, deques are useful in algorithms like sliding window problems, BFS variants, and task scheduling where operations from both ends are needed efficiently.
# Our queue will allows us to store courses with in_degree of 0 (because they have no rerequisites and they are ready to be studied)