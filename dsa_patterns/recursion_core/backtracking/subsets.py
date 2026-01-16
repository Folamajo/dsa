def subsets(nums:list[int])->list[list[int]]:
   subsets = []
   def helper(subset:list[int], start: int):
      subsets.append(list(subset))
      for i in range(start, len(nums)):
         subset.append(nums[i])
         helper(subset, i + 1)
         subset.pop()

   helper([], 0)
   return subsets

if __name__ == "__main__":
   nums = [1,2,3]
   print(subsets(nums))


#  Total number of subsets for n elements is 2^n 
#  Each one will take n work to copy/store so time complexity is (n x 2n)
#  

