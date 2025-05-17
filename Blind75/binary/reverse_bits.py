class Solution:
    # @param n, an integer
    # @return an integer
   def reverseBits(self, n):
      result = 0
      loop= 32

      while loop > 0:
         bit = n & 1
         result = result << 1 
         result = result | bit 
         n = n >> 1 
         loop -= 1 
      
      return result 
        


solution = Solution()
print(solution.reverseBits(0b0000010100101000001111010011100))