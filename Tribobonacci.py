first = 0
second = 0
third = 1

def tribonacci(limit, first, second, third):
    for i in range(limit + 1):
        tribNumber = first + second + third
        print(tribNumber)
        first = second
        second = third
        third = tribNumber

number = int(input("Input: "))

tribonacci(number, first, second, third)