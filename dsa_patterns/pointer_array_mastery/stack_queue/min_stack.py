class MinStack:
   def __init__(self):
      self.stack = []
      self.min = []


   def push(self, val:int)-> None:
      self.stack.append(val)
      
      if len(self.min) == 0 or val < self.min[-1]:
         self.min.append(val)
      else:
         self.min.append(self.min[-1])
      return

   def pop(self)->int:
      if len(self.stack) > 0:
         self.min.pop()
         return self.stack.pop()
      
   def top(self)-> int:
      if len(self.stack) > 0:
         return self.stack[len(self.stack) - 1]
      
   def getMin(self) -> int:
      if len(self.stack) > 0:
         return min(self.stack) 