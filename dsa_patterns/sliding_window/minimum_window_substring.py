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

   need = len(t_count)
   have = 0

   

   return 