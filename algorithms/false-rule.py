import math
import pandas as pd

def false_rule(fun, a, b, tolerance):
    solucion = None
    contador = 0
    error_calculado = 101
    if fun(a) * fun(b) >= 0:
        raise ValueError("La función no cumple con el teorema del valor intermedio en el intervalo [a, b].")
        
    while error_calculado >= tolerance:
        contador += 1
        solucion = a - ((fun(a) * (b - a)) / (fun(b) - fun(a)))
        error_calculado = abs((solucion - a))

        if fun(a) * fun(solucion) >= 0:
            a = solucion
        else:
            b = solucion
    print('La solucion aproximada es: {:.6f}'.format(solucion))
    print('Encontrada en: {:.0f}'.format(contador) + ' iteraciones')    
    print('Con un error relativo de: {:.6f}'.format(error_calculado))


def my_function(x):
    return math.exp(-x) - x

a = 0.0
b = 1.0
tolerance = 1e-6

false_rule(my_function, a, b, tolerance)