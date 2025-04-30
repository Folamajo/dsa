# Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

class Solution(object):
   def countBits(self, n):
      """
      :type n: int
      :rtype: List[int]
      """
      #Brute Force
      ans = [0] * (n + 1)
      binary_values = []
      for i in range(n+1):
         binary = bin(i)[2:]
         binary_values.append(binary)
      
      
      for index, value in enumerate(binary_values):
         count = 0
         for num in value:       
            if num == '1':
               count += 1
            ans[index] = count
      return ans

solution = Solution()
print(solution.countBits(2))