

# QUESTION
# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.


# CONCEPT
# We start by creating a dummy node
# we attach a pointer this node that allows us to determine the tail of the merged list
# We then attach pointers to our two lists 
# We compare the value at each pointer and attach to our dummy node
# We move the pointer from whereever we attached 
# We then attach the left over nodes

#PSEUDOCODE
# Create function title that accepts two lists:
#     Create dummy Node 
#     Create variable tail that points to dummy node 
#     Define while loop while both lists hae nodes:
#        Compare their current values
#        Attach the smaller one to the merged list(tail.next)
#        Move the pointer forward in that list
#        Move tail forward
#     Attach rest of the list to the tail
#     return Merged list head