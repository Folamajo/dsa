def subsetsWithDup(nums: list[int])->list[list[int]]:
   nums.sort() #Aligns duplicates
   result = []

   def backtrack(path, index):
      result.append(list(path))
      for i in range(index, len(nums)):
         if i > index and nums[i] == nums[i - 1]:
            continue
       
         path.append(nums[i])
         backtrack(path, i + 1)
         path.pop()
   backtrack([], 0)
   return result
# In subsets II we must avoid generating duplicate subsets

if __name__ == "__main__":
   nums = [1,2,2]
   print(subsetsWithDup(nums))


   # TIME COMPLEXITY
   # If input array has length n the maximum number of unique subsets that can be generated is O(2 ^ n)
   # If each subset we generate can be up to length n and there are up to 2^n the most accurate time complexity is O(n * 2^n)

   # SPACE COMPLEXITY
   # Maximum space used but the recursion stak and path excluding the output list is O (n)
   # When we include the required to store all subsets the total complexity becomes O(n * 2^n)