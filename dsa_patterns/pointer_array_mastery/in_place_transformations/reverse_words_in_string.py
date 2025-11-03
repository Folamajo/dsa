def reverse_helper(word_list: list)->str:
   left = 0
   right = len(word_list) -1 

   while left < right:
      temp = word_list[left]
      word_list[left] = word_list[right]
      word_list[right] = temp
      left += 1
      right -= 1

   return ' '.join(word_list)


def reverse_words(s:str)->str:
   if len(s) == 1:
      return s

   normalised_string = s.strip().split()
   return reverse_helper(normalised_string)
if __name__ == "__main__":
   input = "a good   example  "
   print(reverse_words(input))


#SPACE COMPLEXITY 
# Our space complexity works out to be O(1)
# Our time complexity is O(1)