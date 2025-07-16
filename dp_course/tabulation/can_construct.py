def can_construct(target, word_bank):
   table = [False] * (len(target))

   for i in range(len(target)):
      if table[i] == False:
         for value in word_bank:
            if target[i] in value:
               table[i] = True

   if False in table:
      return False
   return True


print(can_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd'])) #True
print(can_construct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))  # False
print(can_construct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))  # True  
print(can_construct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"]))  # False  
print(can_construct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee", ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"])) #True
