import numpy as np
from sklearn.svm import SVC

# 2. Agregar el nuevo punto [5, 5] etiquetado como Clase 0
X = np.array([
    [2,2], [3,3], [4,2], [6,6], [7,8], [8,7], [5,5]
    ])
Y = np.array([0, 0, 0, 1, 1, 1, 0])

print("--- EXPERIMENTO 1: KERNEL LINEAL ---")
modelo_lineal = SVC(kernel='linear')
modelo_lineal.fit(X, Y)

print("Vectores de soporte (Lineal):\n", modelo_lineal.support_vectors_)
print("Predicción para [5, 4]:", modelo_lineal.predict([[5, 4]])[0])

print("\n--- EXPERIMENTO 2: KERNEL RBF ---")
modelo_rbf = SVC(kernel='rbf')
modelo_rbf.fit(X, Y)

print("Vectores de soporte (RBF):\n", modelo_rbf.support_vectors_)
print("Predicción para [5, 4]:", modelo_rbf.predict([[5, 4]])[0])

