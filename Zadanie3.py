from math import sqrt

def is_fibonacci(n) -> bool:
    if (sqrt(5*(n**2)-4)%1 == 0) or (sqrt(5*(n**2)+4)%1 == 0):
        return True
    else: return False


print(is_fibonacci(float(input())))
