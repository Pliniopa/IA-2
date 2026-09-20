import numpy as np

def sigmoide(x):
    return 1 / (1 + np.exp(-x))

# 3. El Reto Dimensional: Cambiamos X a una matriz de 2x3 (2 clientes)
X = np.array([
    [0.5, 0.8, 0.2],  # Cliente 1
    [0.1, 0.9, 0.9]   # Cliente 2
])

W1 = np.array([
    [0.1, 0.2, -0.3, 0.4],
    [-0.5, 0.6, 0.7, -0.8],
    [0.9, -0.1, 0.2, 0.3]
])

b1 = np.array([0.1, -0.2, 0.3, -0.4])

# np.dot procesa ambos clientes al mismo tiempo
Z1 = np.dot(X, W1) + b1
A1 = sigmoide(Z1)

print("Z1 (Matriz de 2x4):\n", Z1)
print("\nA1 (Matriz de 2x4):\n", A1)

W2 = np.array([0.5, -0.6, 0.7, 0.8])
b2 = np.array([-0.1])

Z2 = np.dot(A1, W2) + b2
Salida_Final = sigmoide(Z2)

# Imprimimos la probabilidad de ambos clientes (sin np.round para ver los decimales exactos)
print("\nProbabilidad de la red para cada cliente:\n", Salida_Final)

# Si quieres ver la decisión redondeada (0 o 1):
print("\nPredicción final (0 o 1):\n", np.round(Salida_Final))