from sympy import symbols, Eq, solve

x, a, b, c = symbols('x, a, b, c')
print(type)
eq1 = Eq((a+b+c),8)
eq2 = Eq((13+(3*b)+(9*c)),10)
eq3 = Eq((13+(5*b)+(8*c)),11)
print(solve((eq2, eq3), (b, c)))



''' import numpy as np
import numpy.polynomial.polynomial as poly

x = [1, 3, 2]
y = [8, 10, 2]
P1_coeff = [0, 0, 0]
P2_coeff = [0, 3, 9]
P3_coeff = [0, 5, 8]

# get the polynomial function
P1 = poly.Polynomial(P1_coeff)
P2 = poly.Polynomial(P2_coeff)
P3 = poly.Polynomial(P3_coeff)

print(P1)
print(P2)
print(P3) '''

''' def build_polynomial(coeffs, reverse=False):
    abs_coeff = lambda a: abs(a) if abs(a) > 1 else ""
    build_expn = lambda n: "" if n == 0 else ("x" if n == 1 else f"x^{n}")
    plus_minus = lambda idx, a: ("" if a >= 0 else "-") if idx == 0 else (" + " if a >= 0 else " - ")

    coeffs_and_expns = [(coeff, f"{abs_coeff(coeff)}{build_expn(idx)}")
                        for idx, coeff in enumerate(coeffs) if coeff != 0]

    if reverse:
        coeffs_and_expns = reversed(coeffs_and_expns)

    chunks = [f"{plus_minus(idx, coeff)}{expn}"
              for idx, (coeff, expn) in enumerate(coeffs_and_expns)]

    return "".join(chunks)

poly = [-3, 5, 1, 7, 0, -1]
print(poly)
print("---------------------------------------------")
print(build_polynomial(poly))
print("---------------------------------------------")
print(build_polynomial(poly, reverse=True))
print("---------------------------------------------") '''
import numpy as np
from scipy.interpolate import lagrange
from numpy.polynomial.polynomial import Polynomial
x = np.array([2, 4, 5])
y = np.array([1942, 3402, 4414])
poly = lagrange(x, y)
P_coeff = np.array(Polynomial(poly).coef)
reverse_P_coeff = P_coeff[::-1]
P = Polynomial(reverse_P_coeff)
print(P)