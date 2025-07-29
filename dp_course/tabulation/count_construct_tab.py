# write a function countConsruct(target, wordank) that accepts a target string and an array of strings.

# The function should return the number of ways the `target` can be constructred by concatenanting elements of 
# the `wordBank` array.

# You may reuse elements of `wordbank` as many times as needed

def count_construct_tab(target, wordbank):
   table = [0] * (len(target) + 1)
   table[0] = 1

   for i in range(len(table)):
      if table[i] > 0:
         