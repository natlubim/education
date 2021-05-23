a = int(input ('введите сторону a'))
b = int(input ('введите сторону b'))
def slicing(sideA, sideB):
    minSide = min(sideA, sideB)
    maxSide = max(sideA, sideB)

    count = maxSide // minSide
    rest = maxSide % minSide

    print("side a: ", sideA, "; ", "side b: ", sideB, "; ", "count: ", count)

    if rest == 0:
        print("Finish")
        return

    slicing(maxSide - count * minSide, minSide)

slicing(a, b)