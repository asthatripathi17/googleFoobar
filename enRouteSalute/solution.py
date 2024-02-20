def salute(st):
   rightWalker = 0
   noSalute = 0
   for ch in st:
       if ch == '>':
           rightWalker += 1
       elif ch == '<':
           noSalute += rightWalker
   return noSalute * 2
