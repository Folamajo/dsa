# Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

class Solution(object):
   def countBits(self, n):
      """
      :type n: int
      :rtype: List[int]
      """
      #Brute Force — O(n log n)
      # ans = [0] * (n + 1)
      # binary_values = []
      # for i in range(n+1):
      #    binary = bin(i)[2:]
      #    binary_values.append(binary)
      
      
      # for index, value in enumerate(binary_values):
      #    count = 0
      #    for num in value:       
      #       if num == '1':
      #          count += 1
      #       ans[index] = count
      # return ans


      #O(n)
      ans = [0] * (n + 1)
      for i in range(1, n+1):
         ans[i] = ans[i >> 1] + (i & 1)
      return ans


solution = Solution()
print(solution.countBits(5))