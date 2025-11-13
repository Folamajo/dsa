class MinStack:
   def __init__(self):
      self.stack = []
      self.min = {}


   def push(self, val:int)-> None:
      self.stack.append(val)
      
      return

   def pop(self)->int:
      if len(self.stack) > 0:
         return self.stack.pop()
      
   def top(self)-> int:
      if len(self.stack) > 0:
         return self.stack[len(self.stack) - 1]
      
   def getMin(self) -> int:
      if len(self.stack) > 0:
         return min(self.stack) 