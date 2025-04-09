class Solution(object):
    def twoSum(self, nums, target):

      """
      :type nums: List[int]
      :type target: int
      :rtype: List[int]
      """
      #Create a hashmap
      seen = {}


      #Loop through list
      for i in range(len(nums)):
         #Get the value of the remainder
         remainder = target - nums[i]
         #Check if the remainder is in our hashmap
         if remainder in seen:
            #return the index of the remainder and the index of the loop
            return [seen[remainder], i]
         #Else
         else:
            #put the index and value in our current loop in out hashmap
            seen[nums[i]] = i
      
input = [2,7,11,15]
solution = Solution()
print(solution.twoSum(input, 9 ))
