from math import sqrt

def rightTriangle(a, b):
    ans = sqrt(a * a + b * b)
    return ans

print(rightTriangle(1, 1))