def largestRectangleArea(heights:list[int])->int:
   stack = []
   max_area = 0 

   for i in range(len(heights) + 1):
      if heights[i] < 
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