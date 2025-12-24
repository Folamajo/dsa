def largestRectangleArea(heights:list[int])->int:
   stack = []
   max_area = 0 

   for i in range(len(heights) + 1):
      if i == len(heights):
         current_height = 0
      else: current_height = heights[i]

      while stack and current_height < heights[stack[-1]]:
         top = stack.pop()
         top_height = heights[top]
         if len(stack) == 0:
            left_boundary = -1
         else: left_boundary = stack[-1]

         width = i - left_boundary -1 
         area = width * top_height
         if area > max_area:
            max_area = area
      
      stack.append(i)

   return max_area

#CONCEPT
# The stack stores indices in increasing height order
# A bar is removed when a shorter bar appears.
# Popping a bar means we found the boundaries for that bar 
   # Right boundary = current index
   # left bounrdary = stack + 1, if stack is not empty 
   # index 0, if stack is empty
# Width = right boundary - left boundary
# Area = height x width
# Track the maximum area as you pop 
# After the scan ends, we treat the end of the array as the right boundary and pop everything left in the stack the same way. 


# TIME COMPLEXITY 
# a single index can be push into the stack at least once and it can be popped once
# So total stack operations is 2n 
# Even though theres a while loop inside a for loop the total work done by the while loop across the entire run is linear not per iteration
# Time complexity: O(n)

# SPACE COMPLEXITY 
# In the worst case the stack can grow to the size of (n)
# Space complexity: O(n)