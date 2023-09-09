import math
import pandas as pd

def secant(f, x0, x1, tol):

    results = []
    iteration = 0

    while abs(f(x1)) >= tol:
        x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        error = abs(x2 - x1)
        results.append((iteration, x2, f(x2), error))

        x0 = x1
        x1 = x2
        iteration += 1

    df = pd.DataFrame(results, columns=["Iteración", "x", "f(x)", "Error"])
    
    raiz = x1
    
    return df, raiz

# Ejemplo de uso:
def funcion_ejemplo(x):
    return math.exp(-x) - x

x0 = 1
x1 = 0.9
tolerance = 1e-6

pd.options.display.float_format = '{:.10f}'.format
resultados_df, raiz = secant(funcion_ejemplo, x0, x1, tolerance)

# Imprimir el DataFrame y la raíz encontrada
print("Resultados:")
print("\nRaíz aproximada:", raiz)
print(resultados_df)