def can_construct_tab(target, word_bank):
   table = [False] * (len(target) + 1)
   table[0] = True

   for i in range(len(table)):
      if table[i] == True:
         for word in word_bank:
            if target[i : i + len(word)] == word:
               table[i+len(word)] = True

   return table[len(target)]



print(can_construct_tab('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd'])) #True
print(can_construct_tab("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))  # False
print(can_construct_tab("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))  # True  
print(can_construct_tab("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"]))  # False  
print(can_construct_tab("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee", ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"])) #True
