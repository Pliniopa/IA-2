import numpy as np
from sklearn.neighbors import KNeighborsClassifier

X_entrenamiento = np.array([

#edad | salario | hijos
[20,    30,         0],
[22,    35,         1],
[25,    40,         0],

[28,    42,         2],
[30,    45,         1],
[35,    50,         2],
[40,    55,         3],
[42,    60,         2],
[45,    65,         4],
[50,    70,         3]
])

Y_entrenamiento = np.array([
0, 0, 0, 1, 1,
1, 1, 1, 1, 1
])
k = n_neighbors=1

modelo_knn = KNeighborsClassifier(k)

modelo_knn.fit(X_entrenamiento, Y_entrenamiento)

nuevo_cliente = np.array([[30, 40, 5]])

prediccion = modelo_knn.predict(nuevo_cliente)

print("Clase predicha: ", prediccion[0])