def best_sum(target_sum, numbers):
   table = [None] * (target_sum + 1) 
   table[0] = []

   for i in range(target_sum + 1):
      if not table[i] == None:
         for num in numbers:
            new_combination = table[i] + [num]
            if i + num <= target_sum and (table[i + num] == None or len(new_combination) < len(table[i+num])):
               table[i+num] = new_combination
   
   return table[target_sum]
# m = targetSum O(m^2n)
# n = numbers.length O(m^2)