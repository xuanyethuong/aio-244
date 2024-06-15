import math
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
def calc_cos(x, n):
    cos_approx = 0
    for k in range(n + 1):
        term = ((-1) ** k) * (x ** (2 * k)) / math.factorial(2 * k)
        cos_approx += term
    return cos_approx
def calc_sin(x, n):
    sin_approx = 0
    for k in range(n + 1):
        term = ((-1) ** k) * (x ** (2 * k + 1)) / math.factorial(2 * k + 1)
        sin_approx += term
    return sin_approx
def calc_sinh(x, n):
    sinh_approx = 0
    for k in range(n + 1):
        term = (x ** (2 * k + 1)) / math.factorial(2 * k + 1)
        sinh_approx += term
    return sinh_approx
def calc_cosh(x, n):
    cosh_approx = 0
    for k in range(n + 1):
        term = (x ** (2 * k)) / math.factorial(2 * k)
        cosh_approx += term
    return cosh_approx
res_sin = calc_sin(x=3.14 , n =10)
res_sinh = calc_sinh(x=3.14 , n =10)
res_cos = calc_cos(x=3.14 , n =10)
res_cosh = calc_cosh(x=3.14 , n =10)
print("Sin:", res_sin)
print("Sinh:", res_sinh)
print("Cos:", res_cos)
print("Cosh:",res_cosh)