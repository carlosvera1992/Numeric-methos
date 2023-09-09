import math
import pandas as pd

def newton(f, df, x0, tolerance, max_iter):
    data = []

    for i in range(max_iter):
        x1 = x0 - f(x0) / df(x0)
        error = abs(x1 - x0)
        
        data.append({
            "Iteración": i,
            "x": x0,
            "f(x)": f(x0),
            "Derivada(x)": df(x0),
            "Error": error
        })
        
        if error < tolerance:
            return x0, pd.DataFrame(data)
        
        x0 = x1
    
    raise Exception("El método de Newton-Raphson no convergió después de {} iteraciones.".format(max_iter))


def f(x):
    return math.exp(-x) - x

def df(x):
    return - math.exp(-x) - 1

x0 = 1
tolerance = 1e-6
max_iter = 100

pd.options.display.float_format = '{:.10f}'.format

raiz, df_iteraciones = newton(f, df, x0, tolerance, max_iter)

print("Aproximación de la raíz:", raiz)
print("\nTabla de valores:")
print(df_iteraciones)
