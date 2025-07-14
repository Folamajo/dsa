# def can_construct(target, wordbank):
#    if len(target) == 0:
#       return True

   
#    for word in wordbank:
#       # print(word)
#       if target[:len(word)] == word:
#          sliced_target = target[len(word):]

#          result = can_construct(sliced_target, wordbank)

#          if result == True:
#             return True

#       else: 
#          continue

#    return False

# print(can_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))
#TIME COMLEXITY -> 
   #What can shrink in each recursize call 
   #We are going all the way down to empty string O(m + 1 )
   #We are also slicing our target with the amount of values in our wordbank
   # this is O(n)
   # => O(m x n)
#SPACE COMPLEXITY -> 
   # We store our call stack what case scenario that is O(m )
   # We store our string each time we slice is this is also O(m) 
   # O(m^2)



def can_construct(target, wordbank, memo = {}):
   if len(target) == 0:
      return True

   if target in memo:
      return memo[target]
   
   for word in wordbank:
      # print(word)
      if target[:len(word)] == word:
         sliced_target = target[len(word):]

         result = can_construct(sliced_target, wordbank, memo)
         
         if result == True:
            memo[target] = True
            return True
   
   memo[target] = False
   return memo[target]


#CAN CONSTRUCT MEMO
# O(n * m^2) TIME
# O (m^2) SPACE
print(can_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))