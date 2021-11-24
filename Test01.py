from __future__ import division
from __future__ import print_function
from scipy.interpolate import lagrange
from numpy.polynomial.polynomial import Polynomial

import random
import functools
import numpy as np

_PRIME = 1613
_RINT = functools.partial(random.SystemRandom().randint, 0)

def _extended_gcd(a, b):
    """
    Division in integers modulus p means finding the inverse of the
    denominator modulo p and then multiplying the numerator by this
    inverse (Note: inverse of A is B such that A*B % p == 1) this can
    be computed via extended Euclidean algorithm
    http://en.wikipedia.org/wiki/Modular_multiplicative_inverse#Computation
    """
    x = 0
    last_x = 1
    y = 1
    last_y = 0
    while b != 0:
        quot = a // b
        a, b = b, a % b
        x, last_x = last_x - quot * x, x
        y, last_y = last_y - quot * y, y
    return last_x, last_y

def _divmod(num, den, p):
    """Compute num / den modulo prime p

    To explain what this means, the return value will be such that
    the following is true: den * _divmod(num, den, p) % p == num
    """
    inv, _ = _extended_gcd(den, p)
    return num * inv

def _lagrange_interpolate(x, x_s, y_s, p):
    """
    Find the y-value for the given x, given n (x, y) points;
    k points will define a polynomial of up to kth order.
    """
    k = len(x_s)
    assert k == len(set(x_s)), "points must be distinct"
    def PI(vals):  # upper-case PI -- product of inputs
        accum = 1
        for v in vals:
            accum *= v
        return accum
    nums = []  # avoid inexact division
    dens = []
    for i in range(k):
        others = list(x_s)
        cur = others.pop(i)
        nums.append(PI(x - o for o in others))
        dens.append(PI(cur - o for o in others))
    den = PI(dens)
    num = sum([_divmod(nums[i] * den * y_s[i] % p, dens[i], p)
               for i in range(k)])
    return (_divmod(num, den, p) + p) % p

def recover_secret(shares, prime=_PRIME):
    """
    Recover the secret from share points
    (x, y points on the polynomial).
    """
    if len(shares) < 2:
        raise ValueError("need at least two shares")
    x_s, y_s = zip(*shares)
    return  x_s, y_s, _lagrange_interpolate(0, x_s, y_s, prime)

def poly(x, y):
    poly = lagrange(x, y)
    P_coeff = np.array(Polynomial(poly).coef)
    reverse_P_coeff = P_coeff[::-1]
    P = Polynomial(reverse_P_coeff)
    return P

def main():
    print('Input')
    minimum = int(input('Minimum = '))
    sharesTmp = []
    shares = []
    sharesTmp = input('Share secret = ').split('),(')
    sharesTmp = [i.strip('(') for i in sharesTmp]
    sharesTmp = [i.strip(')') for i in sharesTmp]
    for i in range (len(sharesTmp)):
        shares.append((sharesTmp[i]).split(','))
    for i in range (len(sharesTmp)):
        shares[i][0] = int(shares[i][0])
        shares[i][1] = int(shares[i][1])
        shares[i] = tuple(shares[i])
    x, y, secret = recover_secret(shares[:minimum])
    print('Output')
    print("Polynomial = ",poly(x, y))
    print('Secret recovered from minimum subset of shares: ',
          secret)
    x, y, secret = recover_secret(shares[0-(len(shares)-minimum):])
    print("Polynomial = ",poly(x, y))
    print('Secret recovered from a different minimum subset of shares: ',
          secret)

if __name__ == '__main__':                    
    main()