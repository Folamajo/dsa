def search_rotated(nums: list[int], target: int) -> int:
   left = 0 
   right = len(nums) - 1

   while left <= right:
      midpoint = left + int((right - left)/2)

      if nums[midpoint] == target: 
         return midpoint
      
      elif nums[left] > nums[midpoint]: 
         #We know right side is sorted 
         if target > nums[midpoint] and target <= nums[right]
            left = midpoint + 1

      else: #left side is sorted


# In this scenario the rotated side always has one sorted half and one unsorted half 