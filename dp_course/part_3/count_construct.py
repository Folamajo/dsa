def count_construct(target, word_bank, memo={}):
   if target == '':
      return 1
   
   if target in memo:
      return memo[target]
   count = 0
   for word in word_bank:
      if target[:len(word)] == word:
         sliced_target = target[len(word):]

         result = count_construct(sliced_target, word_bank, memo)
         count += result 
   
   memo[target] = count
   return count

print(count_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd', 'abcdef', 'ef']))
# INPUT SIZE ? 
   # m = length of the target string
   # n = number of words in the word bank 
#TIME COMPLEXITY -> how many recursive calls can be made till we get to our base case (m + 1)
#-> how long will it take to for us to slice our target -> word bank legth -> O(n)
# O(m x n)

#SPACE COMPLEXITY -> how many keys do we store in the memo. worst case we store the length of the target 
# What is saved in our call stack -> 