import random
n=int(input("Введите размер списка:\n"))
A=[]
for i in range(n):
    a=random.randint(0,99)
    A.append(a)
s=sum(A)
l=len(A)
a=s/l
print("Элементы списка:")
for i in range(n):
    print(A[i])
print("Сумма элементов: "+str(s))
print ("Среднее арифметическое элементов: "+str(a))







for i in range(n):
    print(A[i])
