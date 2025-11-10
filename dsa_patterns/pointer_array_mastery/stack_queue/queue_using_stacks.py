class MyQueue: 
   def __init__(self):
      self.input = []
      self.output = []

   def push(self, x: int)-> None:
      self.input.append(x)
      return
   
   def pop(self) -> int:
      if len(self.output) == 0 :
         while self.input:
            self.output.append(self.input.pop())

      return self.output.pop()

   def peek(self) -> int | None:
      if len(self.output) == 0 :
         while self.input:
            self.output.append(self.input.pop())

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


#  TIME COMPLEXITY 
#  Since elements is moved at most once between stacks, its total "work" is constant over its entire lifetime. That's why even though a single transfer looks costly, when averaged out over many operations each operations cost O(1)

#  SPACE COMPLEXITY 
# Since the two stacks always hold exactly the elements that are currently in the queue no extra copies hanging around long term the total space of our data structure uses grows linearly with the number of items in the queue So space is O(n)