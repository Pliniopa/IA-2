import numpy as np

def funcion_escalon(z):
    if z >= 0:
        return 1
    else:
        return 0

def perceptron(x, w, b):
    z = np.dot(x, w) + b
    salida = funcion_escalon(z)
    return salida

# --- PARÁMETROS PARA LA COMPUERTA OR ---
pesos = np.array([0.5, 0.5])
sesgo = -0.2

# Probar todas las combinaciones posibles
entradas = [
    np.array([1, 1]),
    np.array([1, 0]),
    np.array([0, 1]),
    np.array([0, 0])
]

print("--- RESULTADOS COMPUERTA OR ---")
for x in entradas:
    resultado = perceptron(x, pesos, sesgo)
    print(f"Entrada {x} -> Salida: {resultado}")