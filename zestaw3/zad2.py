from random import random
A=[[round(random()*100) for y in range(1+4*x,5+4*x)] for x in range(4)]
print(A)
przekatna=[A[x][x]for x in range(4)]
print(przekatna)