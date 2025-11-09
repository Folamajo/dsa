class MyQueue: 
   def __init__(self):
      self.input = []
      self.output = []

   def push(self, x: int)-> None:
      self.input.append(x)
      return
   
   def pop(self) -> int:
      if len(self.output) == 0 :
         for i in range(len(self.input)-1, -1, -1):
            self.output.append(self.input[i])
      
      return self.output.pop()

   def peek(self) -> int | None:
      if len(self.output) == 0:
         for i in range(len(self.input) - 1, -1, -1):
            self.output.append(self.input[i])
      
         return self.output[len(self.output) - 1]

      
      return self.output[len(self.output) - 1]

   def empty(self) -> bool : 
      if len(self.output) == 0  and   len(self.input) == 0:
         return True
      return False 

# A QUEUE is a data structure that follows the First-In, First Out (FIFO) principle
# Enqueue is the operation to add an element to the back of the queue. 
# Dequeue is the operation to remove an element from the front of the queue.

# A STACK is a data structure that follow the Last-In, First-Out(LIFO) principle the last element
# The last one added is the the first one removed. 