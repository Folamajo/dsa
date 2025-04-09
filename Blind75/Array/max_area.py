class Solution(object):
   def maxArea(self, height):
      """
      :type height: List[int]
      :rtype: int
      """
      #start with pointers
      left = 0
      right = len(height) -1 
      #initiate max_area
      max_area = 0
      #initiate while loop
      while left < right:
         #Get current area
         current_area = min(height[left], height[right]) * (right - left)
         if current_area > max_area:
            max_area = current_area

         if height[left] < height[right]:
            left += 1
         elif height[right] < height[left]:
            right -= 1
         else:
            left+= 1
            right-=1
      return max_area
      
      #check if left is less than right then move left
      #check if right is less than left then move right
      #check if both are equal - move both

height = [1,8,6,2,5,4,8,3,7]
solution = Solution()
print(solution.maxArea(height))
