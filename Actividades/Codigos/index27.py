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

entrada = np.array([1 ,1])
pesos = np.array([0.5, 0.5])
sesgo = -0.8
resultado = perceptron(entrada, pesos, sesgo)
print ("el perceptron disparo el valor: ", resultado)