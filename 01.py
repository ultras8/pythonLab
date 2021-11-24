import cmath
import sympy as sym
import random
import functools
from sympy.abc import x
#from IPython.display import display,Math
_prime = 17
_RINT = functools.partial(random.SystemRandom().randint, 0)
minimum = 3
secret = 13
listshare = [(1, 8), (3, 10), (5, 11)]
poly = [secret] + [_RINT(_prime - 1) for i in range(minimum - 1)]
print(poly)
a = poly[0]
b = poly[1]
c = secret

# calculate the discriminant
d = (b**2) - (4*a*c)

# find two solutions
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)

print('The solution are {0} and {1}'.format(sol1,sol2))
