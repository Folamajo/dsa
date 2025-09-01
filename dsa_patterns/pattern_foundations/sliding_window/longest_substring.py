#BRUTE FORCE

# def length_of_longest_substring(string):

#    if len(string) == 1 :
#       return 1

#    max_length = 0 
   
#    for i in range(len(string)):
#       current_substring = []
#       current_substring.append(string[i])
#       for j in range(i+1, len(string)):
#          if string[j] in current_substring:
#             max_length = max(max_length, len(current_substring))
#             break
#          else:
#             current_substring.append(string[j])
#             max_length = max(max_length, len(current_substring))

#    return max_length


def length_of_longest_substring(string): #n is the length of the string
   left = 0
   right = 0
   max_length = 0
   window_chars = set()

   for right in range(len(string)): #Loop will execute n times 
      while string[right] in window_chars: #Left can move n times 
         window_chars.remove(string[left])
         left += 1
      
      window_chars.add(string[right])
      window_size = right - left + 1 
      if max_length < window_size:
         max_length = window_size

   return max_length


#TIME COMPLEXITY 
   #Algorithm uses a sliding window with two pointers. 
   # Right pointer expands the window with n times and the left pointer only advances at most n times so this gives O(n + n)

#SPACE COMPLEXITY
   
print(length_of_longest_substring("abcabcbb"))
print(length_of_longest_substring("bbbbb"))
print(length_of_longest_substring("pwwkew"))
print(length_of_longest_substring("a"))

