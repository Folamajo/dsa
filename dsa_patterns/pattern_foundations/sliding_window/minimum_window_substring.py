def min_window(s:str, t:str)-> str:
   
   if len(t) > len(s):
      return ""
   
   t_count = {}
   for item in t:
      if not item in t_count:
         t_count[item] = 1
      else:
         t_count[item] += 1

   window_count = {}

   left = 0
   right = 0
   min_window = ""

   #Checks if window is valid
   need = len(t_count)
   have = 0

   best_window= float("inf")
   best_start = -1
   best_end = -1 

   for right in range(len(s)):
      curr_char = s[right]
      if not curr_char in window_count:
         window_count[curr_char] = 1
      else:
         window_count[curr_char] += 1

      if curr_char in t_count:
         if window_count[curr_char] == t_count[curr_char]:
            have += 1

      while have == need:
         #Decrement left in our window 
         curr_window_length = right - left + 1 
         if curr_window_length < best_window:
            best_window = curr_window_length
            best_start = left
            best_end = right   

         c = s[left]
         window_count[c] -= 1

         if c in t_count and window_count[c] < t_count[c]:
            have -= 1
         left += 1


         
   if best_start == -1:
      return ""
   else:
      return s[best_start : best_end + 1]


if __name__ == "__main__":
   print(min_window("ADOBECODEBANC", "ABC"))