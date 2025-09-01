def remove_duplicates(nums: list):

   left = 0
   right = 1

   for right in range(len(nums) - 1):
      while nums[left] == nums[right]:
         del nums[right]
         nums.append("_")
      
      left += 1
      right += 1
      return nums  
         # nums[right] = nums[right + 1]
         # temp = right
         # nums[right] = nums[right + 1]
         # nums[right + 1] = temp
         # nums[right] = "_"
         # nums[right] = temp
      # left += 1
      # right += 1

      
   
   


input = [1,1,1,1,1,1,2,2,2,2]
print(remove_duplicates(input))