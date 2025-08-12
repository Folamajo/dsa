def length_of_longest_substring(string):

   if len(string) == 1 :
      return 1

   max_length = 0 
   
   for i in range(len(string)):
      current_substring = []
      current_substring.append(string[i])
      for j in range(i+1, len(string)):
         if string[j] in current_substring:
            max_length = max(max_length, len(current_substring))
            break
         else:
            current_substring.append(string[j])
            max_length = max(max_length, len(current_substring))

   return max_length


print(length_of_longest_substring("abcabcbb"))
print(length_of_longest_substring("bbbbb"))
print(length_of_longest_substring("pwwkew"))
print(length_of_longest_substring("a"))

