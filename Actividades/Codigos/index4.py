import numpy as np

A = np.array([
    [10, 20, 30, 40],
    [40, 50, 60, 70],
    [10, 20, 30, 40],
    [40, 50, 60, 70]
])

a_transpuesta = A.T

vector_1D = A.flatten()

print("Forma Original:", A.shape)
print(" ")
print("Forma Transpuesta: ", a_transpuesta.shape)
print(" ")
print("vector plano: ", vector_1D)