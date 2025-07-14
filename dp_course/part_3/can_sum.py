#Write a function canSum(targetSum, numbers) that takes in a targetSum and an array of numbers as arguments. The function should return a #boolean indicating whether or not it is possible to generate the targetSum using numbers from the array. You may use an element of an #array as many times as needed. You may assume that all numbers are nonnegative.


def can_sum(target, num_list, memo = {}):
   #Establish the base case 
   if target == 0:
      return True
   if target < 0:
      return False
   
   if target in memo:
      return memo[target]
   
   for i in range(len(num_list)):
      check = can_sum((target - num_list[i]), num_list, memo)
      if check == True:
         memo[target] = check 
         return memo[target]
      else: 
         continue
   
   
   memo[target] = False
   return memo[target]
   

print(can_sum(1, [5,3,4,7]))


#GET THE HEIGHT




#CHAT GPT
#TIME COMPLEXITY: The smallest possible step we can take at each recursive call is subtracting the smallest number in the list
#Target / smallest number in the list
#We wont create more that target different subproblems 
#Number of unique subproblems is O(target)
#For each target value we are doing n recurseive calls where n = (len(num_list))
#The work per subproblem is O(n)
# So we have O(target) unique subproblems, Each one does O(n) word -> O(target x n)


#SPACE COMPLEXITY
#Memo Size : stores one entry per unqiue target value
# Max possible target values go from down to 0 
#Total entires = O(target)
#For the call stack depth
#We keep subtracting the smallest number until we hit 0 or less
# so depth stack is O(target)
#Final Space complexity O(target)  — from both memo and recrusion depth.