import math
import pandas as pd
from flask import Flask, render_template_string, send_file
import matplotlib.pyplot as plt
import numpy as np
from io import BytesIO

app = Flask(__name__)

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
        elif fa * fxm < 0:
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

# Crear una página HTML para mostrar la tabla de valores y el gráfico
html_template = """
<!DOCTYPE html>
<html>
<head>
    <title>Tabla de Valores y Gráfico de la Función</title>
</head>
<body>
    <h1>Tabla de Valores de la Función</h1>
    {{ table_data.to_html(classes="table table-striped", render_links=True, escape=False) | safe }}
    
    <h1>Gráfico de la Función</h1>
    <img src="{{ graph_image }}" alt="Gráfico de la Función">
</body>
</html>
"""

# Ruta para mostrar la página web
@app.route('/')
def show_table():
    # Crear el gráfico de la función
    x = np.linspace(0, 1, 400)
    y = [my_function(xi) for xi in x]
    plt.figure()
    plt.plot(x, y, label='Función: exp(-x) - x', color='blue')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(root, color='gray', linestyle='--', linewidth=0.5, label='Aproximación de la raíz')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Gráfico de la Función y Aproximación de la Raíz')
    plt.legend()
    
    # Guardar el gráfico en un objeto BytesIO
    img_buf = BytesIO()
    plt.savefig(img_buf, format='png')
    img_buf.seek(0)
    
    # Convertir el gráfico en una URL base64
    graph_url = "data:image/png;base64," + img_buf.read().encode('base64').decode()
    
    return render_template_string(html_template, table_data=table_df, graph_image=graph_url)

if __name__ == '__main__':
    app.run(debug=True)




    # # Cálculo y gráfico del error después de que termine el algoritmo
    # errors = []
    # for i in range(iterations):
    #     xm = (a + b) / 2
    #     if my_function(xm) == 0:
    #         break
    #     elif my_function(a) * my_function(xm) < 0:
    #         b = xm
    #     else:
    #         a = xm
    #     errors.append(abs(b - a))

    # plt.plot(range(len(errors)), errors)
    # plt.xlabel('Iteración')
    # plt.ylabel('Error')
    # plt.title('Convergencia del error en el método de la bisección')
    # plt.grid(True)
    # plt.show()


    # # Graficar la función y la convergencia de la bisección
    # x = np.linspace(0, 2, 400)
    # y = [my_function(xi) for xi in x]

    # plt.figure(figsize=(10, 6))

    # # Graficar la función
    # plt.plot(x, y, label='Función: exp(-x) - x', color='blue')

    # # Marcar la raíz encontrada
    # plt.scatter(root, my_function(root), color='red', marker='o', label='Aproximación de la raíz')

    # plt.axhline(0, color='black', linewidth=0.5)
    # plt.axvline(root, color='gray', linestyle='--', linewidth=0.5, label='Aproximación de la raíz')

    # plt.xlabel('x')
    # plt.ylabel('f(x)')
    # plt.title('Gráfico de la función y aproximación de la raíz')
    # plt.legend()
    # plt.grid(True)
    # plt.show()