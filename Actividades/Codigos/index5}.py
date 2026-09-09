import numpy as np

# Matriz de imagen (reemplazar con los valores del diagrama)
I = np.array([
    [100, 100, 100],
    [100, 200, 100],
    [100, 100, 100]
])

# Kernel (reemplazar con los valores del diagrama)
K = np.array([
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0]
])

# Producto Hadamard (elemento a elemento)
resultado = I * K

# Suma de todos los elementos
pixel_central = np.sum(resultado)

print("Matriz resultante:")
print(resultado)

print("\nValor del píxel central:", pixel_central)