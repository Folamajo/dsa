# class Solution(object):
#    def getSum(self, a, b):
#       """
#       :type a: int
#       :type b: int
#       :rtype: int
#       """
      
#       while b != 0:
#          current_sum = a ^ b
#          carry = (a & b) << 1
#          a = current_sum
#          b = carry

#       return a
    

# solution = Solution()
# print(solution.getSum(-1,1))

# Binary 0b tells python that the number is written in binary
# The 32 bit number comes after 32 bits 
#

num = -20
bin_representation = bin(num)
print(bin_representation)