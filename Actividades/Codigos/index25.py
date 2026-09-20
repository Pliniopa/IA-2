import numpy as np
from sklearn.svm import SVC

x = np.array ([
    [2,2],
    [3,3],
    [4,2],
    [6,6],
    [7,8],
    [8,7]
])

y = np.array ([0, 0, 0, 1, 1, 1])

modelo_svm = SVC(kernel="linear")

modelo_svm.fit(x, y)

vectores = modelo_svm.support_vectors_
print("Los vectores de soporte son\n", vectores)

nuevo_punto = np.array([[5,4]])
pred = modelo_svm.predict(nuevo_punto)

print(f"El punto {nuevo_punto} pertenece a la clase: ", pred[0])