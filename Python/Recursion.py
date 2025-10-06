import math
def Recurion_String_Start(a,b):
    return helper_Recursion(a,b, 0)

def helper_Recursion(a,b,index):
    if len(b) > len(a):
        return -1
    sub= a[:len(b)]
    if sub == b:
        return index
    a = a[1:]
    index += 1
    return helper_Recursion(a,b, index)

def sqaureRoot(x):
    return squareRootGuess(x, 1)

def squareRootGuess(x, g):
    if math.isclose(x, g**2):
        return g // 1
    else:
        g = (g + (x/g)) / 2
    return squareRootGuess(x, g)
