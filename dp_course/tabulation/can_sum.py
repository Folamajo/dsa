#Write a function canSum(targetSum, numbers) that takes in a targetSum and an array of numbers as arguments.
#The function should return a #boolean indicating whether or not it is possible to generate the targetSum 
#using numbers from the array. You may use an element of an #array as many times as needed. 
#You may assume that all numbers are nonnegative.

#Unlike the recursion version, we are building a table of boolean values. 
def can_sum(target, numbers):
   #create table 
   table = [False] * (target + 1)
   #initialise base case
   table[0] = True

   #Initialise loop 
   for i in range(len(table)):
      if table[i]:
         for num in numbers:
            if i + num <= target:
               table[i+num] = True 

   return table[target]


print(can_sum(7, [2,3]))
# m = targetSum
# n = len(numbers)
# O(m * n ) time * space