from random import random, randit
dim = 5
largo = 10
pas = [0]*dim

def paso(pos, dim):
   d = randit(0, dim-1)
   pas += -1 if random() < 0.5 else 1
   return pos
   
for t in range(largo):
   pas = paso(pas, dis)
   print pas
