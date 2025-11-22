def search_insert(nums:list, target: int) -> int:
   left = 0
   right = len(nums) - 1

   while left <= right:
      middle = left + int((right - left) / 2)

      if target == nums[middle]:
         return middle
      elif target > nums[middle]:
         left = middle + 1
      else :
         right = middle - 1
   return left


if __name__ == "__main__":
   nums = [1,3,5,6]
   print(search_insert(nums, 4))