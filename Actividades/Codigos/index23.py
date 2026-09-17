import numpy as np
from sklearn.neighbors import KNeighborsClassifier

X_entrenamiento = np.array([
    [20, 30],
    [40 , 50],
    [35, 45]
])

Y_entrenamiento = np.array([0, 1, 1])

modelo_knn = KNeighborsClassifier(n_neighbors=3)

modelo_knn.fit(X_entrenamiento, Y_entrenamiento)

nuevo_cliente = np.array([[30, 40]])

prediccion = modelo_knn.predict(nuevo_cliente)

print("Clase predicha: ", prediccion[0])