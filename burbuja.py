import random

A=[]

for i in range(10):
  valor=random.randint(10,99)
  A.append(valor)

A=[70, 81, 47, 17, 41, 99, 47, 17, 89, 69]
for i in range(1,10):
  for j in range(10-i):
    if A[j]>A[j+1]:
      valor=A[j]
      A[j]=A[j+1]
      A[j+1]=valor
    print(f"({i},{j}) {A}")   # <---- Aquí!!

print(A)
print("burbuja correcto")
print("print en PC1")
