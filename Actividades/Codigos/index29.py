import numpy as np

def sigmoide(x):
    return 1 / (1 + np.exp(-x))

X = np.array([0.5, 0.8, 0.2])

W1 = np.array([
    [0.1, 0.2, -0.3, 0.4],
    [-0.5, 0.6, 0.7, -0.8],
    [0.9, -0.1, 0.2, 0.3]
])

b1 = np.array([0.1, -0.2, 0.3, -0.4])

Z1 = np.dot(X, W1) + b1
A1 = sigmoide(Z1)

W2 = np.array([0.5, -0.6, 0.7, 0.8])
b2 = np.array([-0.1])

Z2 = np.dot(A1, W2) + b2
Salida_Final = sigmoide(Z2)

print ("Prediccion de la red (probabilidad): ", 
       np.round(Salida_Final[0]))

