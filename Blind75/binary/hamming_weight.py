class Solution(object):
   def hammingWeight(self, n):
      """
      :type n: int
      :rtype: int
      """
      check = {}
      #Convert to binary and slice 
      binary = bin(n)[2:]
      binary_list = list(binary)
      # split = binary.split(", ")

      # print(binary_string)
      for i in binary_list:
         if i == "1" :
            if i in check:
               check[i]+= 1
            else:
               check[i] = 1

      return check["1"]

solution = Solution()
print(solution.hammingWeight(2147483645))