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
   bext_end = -1 

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
         


   return 