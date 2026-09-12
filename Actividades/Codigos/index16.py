import numpy as np

# 1. Matriz de imagen definida explícitamente en uint8
I = np.array([
    [10,  20, 30],
    [15, 250, 15],
    [20,  10, 20]
], dtype=np.uint8)

# 2. Kernel de media (mantiene float32 para no perder precisión en la división)
K = np.ones((3, 3), dtype=np.float32) / 9.0

# Se calcula la suma en flotante y se redondea a uint8
zum = I * K
print(zum)
print()
suma_flotante = np.sum(zum)
nuevo_pixel_numpy = np.uint8(np.round(suma_flotante))

print(f"NumPy (uint8): {nuevo_pixel_numpy}")
# Salida: 43
