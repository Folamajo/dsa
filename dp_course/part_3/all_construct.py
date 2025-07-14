#Write a function `all_construct(target, word_bank)` that accepts a target string and an array of strings. 
#The function should return a 2D array containing all of the ways that the `target` can be constructred by the concatenating elements of 
#the `word_bank` array. Each element of the 2D array should represent one combination that constructs the `target`.

#WITHOUT MEMO
def all_construct(target, word_bank):
   if target == '':
      return [[]]

   output = []

   for word in word_bank:
      if target[:len(word)] == word:

         sliced_target = target[len(word):]
         result = all_construct(sliced_target, word_bank)


         result_list = [[word] + sublist for sublist in result]

         for list in result_list:
            output.append(list)

   return output

#WITH MEMO
def all_construct(target, word_bank, memo = {}):
   if target == '':
      return [[]]

   output = []

   if target in memo:
      return memo[target]
   
   for word in word_bank:
      if target[:len(word)] == word:

         sliced_target = target[len(word):]
         result = all_construct(sliced_target, word_bank, memo)
        
         
         result_list = [[word] + sublist for sublist in result]

         for list in result_list:
            output.append(list)
   memo[target] = output
   return output
print(all_construct('purple', ['purp', 'p', 'ur', 'le','purpl']))


         # for list in result:
         #    list.append(word)
         
         
         # print(result)
         # memo[target] = [word]
         # if result == [[]]:
         #    for list in result:
         #       list.append(word)

         # return result