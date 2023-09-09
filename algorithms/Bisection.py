import math
import pandas as pd

def bisection(func, a, b, tol):
    if func(a) * func(b) >= 0:
        raise ValueError("La función no cumple con el teorema del valor intermedio en el intervalo [a, b].")

    iterations = 0
    table_data = []

    while abs(b - a) > tol:
        xm = (a + b) / 2
        fa = func(a)
        fb = func(b)
        fxm = func(xm)
        error = abs(b - a)

        table_data.append([iterations, a, b, xm, fa, fb, fxm, error])

        if fxm == 0:
            return xm, iterations
        
        if fa * fxm < 0:
            b = xm
        else:
            a = xm
        iterations += 1

    root = (a + b) / 2
    table_data.append([iterations, a, b, xm, fa, fb, fxm, error])

    # Crear DataFrame para la tabla de valores
    columns = ['Iteración', 'a', 'b', 'xm', 'f(a)', 'f(b)', 'f(xm)', 'Error']
    table_df = pd.DataFrame(table_data, columns=columns)

    return root, iterations, table_df


# Definición de la función que quieres encontrar la raíz
def my_function(x):
    return math.exp(-x) - x

a = 0.0
b = 1.0
tolerance = 1e-6

root, iterations, table_df = bisection(my_function, a, b, tolerance)

print("Aproximación de la raíz:", root)
print("\nTabla de Valores de la Función:")
print(table_df)