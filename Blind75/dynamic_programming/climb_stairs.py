class Solution(object):
   def climbStairs(self, n):
      """
      :type n: int
      :rtype: int
      """
      if n == 1 or n == 0:
         return 1
      
      prev1 = 1 
      prev2 = 1 
      
      # representing f(0)
      # representing f(1)
      for i in range(2, n+1):
         current = prev1 + prev2
         prev2 = prev1
         prev1 = current

         return current
   
solution = Solution()
print(solution.climbStairs(4))

# Time Complexity: because we are looping from 2 is O(n-1) we turn this to O(n)
# Space complexity because we are storing variables prev1, prev2 and current this is O(1)