# Given integer n, returns True or False based on reachabilty of goal
def bears(n: int) -> bool:
    if n == str(n):
        raise ValueError
    if n == 42:
        return True
    t = n
    if n % 5 == 0:
        temp = n - 42
        if temp >= 42:
            n = temp
    if n % 2 == 0:
        temp = n//2
        if temp >= 42:
            n = temp
    if n % 3 == 0 or n % 4 == 0:
        x = str(n)
        y = list(x)
        z = int(y[-1])* int(y[-2])
        temp = n - z
        if temp >= 42:
            n = temp
    if n == t:
        return False
    return bears(n)

