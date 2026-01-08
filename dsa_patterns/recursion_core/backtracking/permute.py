def permute(nums: list[int])-> list[list[int]]:
   permutations = []

   def helper(partialPerm: list[int]):
      # base case
      if len (partialPerm) == len(nums):
         permutations.append(list(partialPerm))
         return 
      
      for num in nums:
         if not num in partialPerm:
            partialPerm.append(num)
            helper(partialPerm)
            partialPerm.pop()

   helper([])
   return permutations

if __name__ == "__main__":
   nums = [1,2,3]
   print(permute(nums))
# CONCEPT
# A permutation is complete when it contains every number exactly once and its length matches the original input size
# a number can be added to the partial permutation if the number doesnt already exist in the partial permutation and if it is   present in the original input
# each choice represents one branch in the decision tree
# once that branch is fully explored, keeping the choice would block access to sibling branches
# removing it resets the state so you can explore alternative possibilities from the same level
# Each depth represents one position being filled in a single permutation the deepest level will give us all possible values in a single permutation


#  Back tracking works because at every step we only make valid choices. 
#  The moment a choice violates the rules that branch never exists.
#  So the algoritm constructs only legal permutations from the start.
# We need a helper function whose job is to explore permutations from a given state
# A permutatun is complete when: 
# - It contains every number exactly once
# - its length matches the original input 