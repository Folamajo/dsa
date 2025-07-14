# Write a function 'howSum(targetSum, numbers)' that takes in a targetSum and an array of numbers as arguments.
# The function should return an array containing any combination of elemenets that 
# add up to exactly the targetSum. If there is no combination that adds up to the targetSum, then return null.
# If there are multiple combinations possible, you may return any any single one. 



def how_sum(target, numbers):
   table = [None] * (target + 1)
   table[0] = []

   for i in range(target + 1):
     if not table[i] == None:
        for num in numbers:
           if i + num <= target and (table[i+num] == None):
              table[i + num] = table[i] + [num]
           
   return table[target]

print(how_sum(7, [5,3,4,7]))
print(how_sum(8, [2, 3, 5]))
print(how_sum(7, [2, 4]))