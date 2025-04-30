class Solution(object):
   def getSum(self, a, b):
      """
      :type a: int
      :type b: int
      :rtype: int
      """
      
      while b != 0:
         current_sum = (a ^ b) & 0xFFFFFFFF
         carry = (a & b) << 1 & 0xFFFFFFF
         a = current_sum 
         b = carry

      if a <= 0x7FFFFFFF:
         return a 
      else:
         return a - (1 << 32)
      
    

solution = Solution()
print(solution.getSum(2,3))

# Binary 0b tells python that the number is written in binary
# The 32 bit number comes after 32 bits 
