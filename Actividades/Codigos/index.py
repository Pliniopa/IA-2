import numpy as np

A = np.array([
    [10, 20, 10],
    [15, 30, 15],
    [10, 20, 10]

], dtype =np.float32)

alpha = 2.5
beta = 50.0

A_nueva = (alpha * A) + beta

print ("Matriz Nueva:")
print (A_nueva)