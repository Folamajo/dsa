
class TrieNode:
   def __init__(self):
      self.children = {}
      self.is_end = False

class Trie: 
   def __init__(self):
      self.root = TrieNode()

   
   def insert(self, word):
      
# Setting up trie

# A trie is used for effcient prefix-based search
# storing strings character by character
# Fast lookup (better than brute force string comparisons)
# Each node = a character
# Paths = words
# Words share prefixes –> saves space

# Compared to a HashMap a trie allows effcient prefix-based searching
# A trie is built from nodes and each node needs to store:
   # Links to children (next characters)
   # Whether the node marks the end of a word
   # A trie must store a mapping of characters –> child nodes and a boolean for end of word