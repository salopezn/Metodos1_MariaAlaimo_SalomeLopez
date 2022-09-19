

#para el factorial de 4: 
import math

def factorial(integer):
    if integer == 0:
        return 1
    elif integer < 0:
        return 'The integer must be a positive number'
    elif integer > 0:
        return math.prod(range(2, integer + 1))



import sympy as sym
from sympy import integrate
x= sym.Symbol("x")
h=sym.Symbol("h")
p=x*(x-h)*(x-2*h)*(x-3*h)
inte=integrate(p,(x,0,3*h))
derivada=sym.Symbol("F(4)")
error=(derivada/factorial(4))*inte
print(error)