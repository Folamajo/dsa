def search_rotated(nums: list[int], target: int) -> int:
   left = 0 
   right = len(nums) - 1

   while left <= right:
      midpoint = left + int((right - left)/2)

      if nums[midpoint] == target: 
         return midpoint
      
      elif nums[left] <= nums[midpoint]: #checks if left side is sorted 
         if target >= nums[left] and target < nums[midpoint]:
            right = midpoint - 1
         else :
            left = midpoint + 1
      else:
         if target > nums[midpoint] and target <= nums[right]:
            left = midpoint + 1
         else:
            right = midpoint - 1

   return -1 
# In this scenario the rotated side always has one sorted half and one unsorted half 

if __name__ == "__main__":
   nums = [4,5,6,7,0,1,2]
   target = 0
   print(search_rotated(nums, target))