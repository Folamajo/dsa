# Write a function 'howSum(targetSum, numbers)' that takes in a targetSum and an array of numbers as arguments.
# The function should return an array containing any combination of elemenets that 
# add up to exactly the targetSum. If there is no combination that adds up to the targetSum, then return null.
# If there are multiple combinations possible, you may return any any single one. 

#RECURSION
# def howSum(targetSum, numbers):
#    if targetSum == 0:
#       return []
#    if targetSum < 0:
#       return None
   

#    for num in numbers:
#       remainder = targetSum - num
#       remainderResult = howSum(remainder, numbers)
#       if not remainderResult == None:
#          remainderResult.append(num)
#          return remainderResult
#    return None

#MEMOIZATION

def howSum(targetSum, numbers, memo={}):
   if targetSum == 0:
      return []
   if targetSum < 0:
      return None
   
   if targetSum in memo:
      return memo[targetSum]
   
   for num in numbers: 
      remainderResult = howSum(targetSum - num, numbers, memo)

      if not remainderResult == None: 
         
         resultList = remainderResult + [num]
         memo[targetSum] = resultList
         print(memo) 
         return memo[targetSum]
  
   memo[targetSum] = None 
   return memo[targetSum]


print(howSum(7, [5,3,4,7]))


#RECURSION
#Recursive if target is == 0 we are returning an empty list because we are saying no combination of value in our list is equal to 0 since we have positive values in our list
#If our target < 0 we return null -> no combination in our list can get a negative number
#After base case -> loop through the list, check each number and combination.
#We check what number in the list can be used to breakdown our target sum until we reach 0 
#store number in a final list which we will return after recursion 
#concatenate so we achieve the combination in the return
#return to user 

# PROBLEM WITH RECURSION 
# Inefficient because in the worst case scenario 
# we are recompution the same problems over and over for different path 
# especially as the target decreases slowly
# this gives a huge recursion tree — exponential time

# SOLUTION
# Memoization: It allows us to cache the combinations we already solved 
# we can check the result in our cache 
# Time complexity goes from explosive to linear with respect tto the target. -> (O(targetSum x n))
#SPACE COMPLEXITY: Memo dictionary: O(targetSum), Call stack: O(targetSum), Result list: O(targetSum) -> O(targetSum)