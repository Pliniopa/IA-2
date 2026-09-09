import numpy as np

a = np.random.randint(200, 255, (5,5))


print (a)


alfa = 0.5
beta = -50.0

a_nueva = (alfa * a) + beta

a_nueva = np.clip(a_nueva, 0, 255)

print("")

print(a_nueva)

a_nueva = a_nueva.astype(np.uint8)
print("")
print(a_nueva)