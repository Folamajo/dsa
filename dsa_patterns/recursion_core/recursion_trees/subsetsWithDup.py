def subsetsWithDup(nums: list[int])->list[list[int]]:
   nums.sort() #Aligns duplicates
   result = []

   def backtrack(path, index):
      result.append(path)
      for i in range(index, len(nums)):
         if i > index and nums[i] == nums[i - 1]:
            continue
       
         path.append(nums[i])
         backtrack(path, i + 1)
         path.pop()
   backtrack([])
   return result
# In subsets II we must avoid generating duplicate subsets

if __name__ == "__main__":
   nums = [1,2,2]
   print(subsetsWithDup(nums))