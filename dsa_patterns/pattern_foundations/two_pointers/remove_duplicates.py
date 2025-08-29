def remove_duplicates(nums: list):

   left = 0
   right = 1

   for left in range(len(nums)):
      if nums[left] == nums[right]:
         temp = nums[right + 1]
         nums[right] = '_'
         return nums
         # nums[right] = "_"
         # nums[right] = temp
         
   
   


input = [1,1,2]
print(remove_duplicates(input))