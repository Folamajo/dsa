def hasCycle(head):



if __name__ == "__main__" :
   input = [3, 2, 0, -4]

# WHAT IS A LINKED LIST CYCLE
# A linked list has a cycle if there is a node in the list that we continuously reach when we keep following the next pointer
# so usually in a linked list if we keep following the pointer we would reach null.  In this case we would just end up back at one of the nodes

# BRUTE FORCE
# This involves using a hash map that stores each node we see and if we come across a code we have already seen we know its a cycle
# or if we reach null we know theres no cycle

# FASTER SOLUTION
# Floyd's cycle detection
# Move one pointer slowly (one step at a time) and another pointer faster(two steps at a time)