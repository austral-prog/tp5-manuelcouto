import math


def roots(a, b, c):
    resu=0
    if (b**2-4*a*c)<0:
        resu=()
    else:
        r1 = (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
        r2 = (-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
        if r1==r2:
            resu=(r1)
        elif r1!=r2:
            resu=(r1,r2)
    return resu


def value_y(a, b, c, x):
    resu=a*(x**2)+b*x+c
    return resu

def to_string(a, b, c):
    resu=0
    if a != 0 and b != 0 and c != 0:
       resu=f"f(x) = {a} * X^2 + {b} * X + {c}"
    elif a != 0 and b == 0 and c != 0:
        resu = f"f(x) = {a} * X^2 + {c}"
    elif a==0 and b!=0 and c!=0:
        resu=f"f(x) = {b} * X + {c}"
    elif a != 0 and b != 0 and c == 0:
        resu = f"f(x) = {a} * X^2 + {b} * X"
    elif a == 0 and b == 0 and c != 0:
        resu = f"f(x) = {c}"
    elif a == 0 and b != 0 and c == 0:
        resu = f"f(x) = {b} * X"
    elif a != 0 and b == 0 and c == 0:
        resu = f"f(x) = {a} * X^2"
    return resu


def derivation(a, b, c):
    resu=0
    if a!=0 and b!=0:
        resu=f"f'(x) = {2*a} * X + {b}"
    elif a!=0 and b==0:
        resu = f"f'(x) = {2 * a} * X"
    elif a==0 and b!=0:
        resu = f"f'(x) = {b}"
    elif a==0 and b==0:
        resu=f"f'(x) = 0"
    return resu
