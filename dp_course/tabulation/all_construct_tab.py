# write function that accepts a target string and an array of strings. 
# Return a 2D array containing all of the ways that the 'target' can be constructed by concatenating elements of the 'wordBank' array


def all_construct(target, word_bank):
   table = [None] * (len(target) + 1) 
   table[0] = [[]]

   for i in range(len(table)):
      if not table[i] == None:
         for word in word_bank:
            if target[i : i + len(word)] == word:
               for word_list in table[i]:
                  new_combination = word_list + [word]
                  if table[i + len(word)] == None:
                     table[i + len(word)] = []
                  
                  table[i + len(word)].append(new_combination)
               # table[i : ]
   return table[len(target)]
print(all_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd', 'ef', 'c']))

# TIME COMPLEXITY = O (m * n * W)
# m: loop over wordBank
# n: max path length / string copying
# W: total number of possible combinations

# SPACE COMPLEXITY = 0(n * W)
# W = total number of valid combinations
# n = maximum number of words per combination (since target length is n )