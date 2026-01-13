def subsets(nums:list[int])->list[list[int]]:
   subsets = []
   def helper(subset:list[int], start: int):
      subsets.append(list(subset))

if __name__ == "__main__":
   nums = [1,2,3]
   print(subsets(nums))