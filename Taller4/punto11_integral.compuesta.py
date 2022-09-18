import numpy as np
limitea = -1
limiteb = 1
h = 9999
def func (x):
    f=np.sqrt((1+(np.exp(-(x**2)))))
    return f
def calculate (limitea, limteb, h):
    suma = func(limitea) + func(limiteb)
    tamaño = ((limiteb - limitea) / h)
    for i in range(1, h):
        if (i % 3 == 0):
            suma = suma + 2 * func(limitea + i * tamaño)
        else:
            suma = suma + 3 * func(limitea + i * tamaño)
    return ((float( 3 * tamaño) / 8 ) * suma)
integral= calculate(limitea, limiteb, h)

print(integral)
