# write a function countConsruct(target, wordank) that accepts a target string and an array of strings.

# The function should return the number of ways the `target` can be constructred by concatenanting elements of 
# the `wordBank` array.

# You may reuse elements of `wordbank` as many times as needed

def count_construct_tab(target, wordbank):
   table = [0] * (len(target) + 1)
   table[0] = 1

   for i in range(len(table)):
      if table[i] > 0:
         for word in wordbank:
            if target[i : i + len(word)] == word:
               table[i + len(word)] += table[i]

   return table[len(target)]


print(count_construct_tab('purple', ['purp', 'p', 'ur', 'le', 'purpl']))




# Time complexity:
#    What causes time to grow : 
#       - How many steps your loop runs
#       - What happens inside each step 

#    In this scenario: our outer loop -> for i in range(len(table)):
#        runs the length of of our table 
#        result in OUTER LOOP = O(n)
#        For our inner loop we have "m" values in the wordbank ->  for word in wordbank:
#           our loop will run "m" times
#           results in inner loop = O(m)
#        So far we have O(n * m )
#        we have target[i : i + len(word)] == word 
#        we are slicing the string -> slicing a string of length k take O(k) times
#        so we have O(len(word))
#        TOTAL TIME COMPLEXITY =>  O(n * m * L)


# SPACE COMPLEXITY 
# we are storing our length of the of the table we constucted
# table = [0] * (len(target) + 1 )
# Space = O(n)