#1.1
''''
import math

def f(x, y):
    z = 5**(2*x*y) - x**5*x - math.e**(-x**2)
    return z

x = 0.3
y = 1
z = f(x, y)
print(z)
# 1.3

import math

def f(x, t):
    z = math.sqrt((math.cos(x)**2 + math.sin(x)**2) / (35 * x * t))
    return z

t = 3
x = 1
z = f(x, t)
print(z)
'''
#1.2
'''''
import math

def f(x, y):
    z = (x + 4) ** (1/3) - math.atan(x*y / 3*y+1)**2
    return z

y = 2
x = 2
z = f(x, y)
print(z)
'''
#1.4

import math

def f(x, y):
    z = (abs(x)+1)/(3*2) + (math.e**(-3*x)-0.4) / (5+7*y)
    return z

y = 3
x = 3
z = f(x, y)
print(z)