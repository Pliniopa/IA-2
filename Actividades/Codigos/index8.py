import cv2
import matplotlib.pyplot as plt

imagen = r"\Muestra.png"
imagen_c = cv2.imread(imagen, cv2.IMREAD_GRAYSCALE)

histograma = cv2.calcHist([imagen_c], [0], None, [256], [0, 256])

plt.plot(histograma)
plt.title("Distribucion de intensidad")
plt.xlabel("valor del pixel (0 - 255)")
plt.ylabel("Frecuencia (cantidad de pixeles)")
plt.show()