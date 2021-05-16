mas=[0,99]
maximum=mas[0]
for i in range(1,len(mas)):
    if mas[i]>maximum:
        maximum=mas[i]
print(maximum)
