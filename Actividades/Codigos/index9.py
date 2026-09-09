import cv2
import matplotlib.pyplot as plt

# Cargar imagen en color (BGR)
imagen = cv2.imread(r"C:\Test\py\Muestra.png")

if imagen is None:
    print("No se pudo cargar la imagen")
    exit()

# Calcular histogramas de cada canal
hist_azul = cv2.calcHist([imagen], [0], None, [256], [0, 256])
hist_verde = cv2.calcHist([imagen], [1], None, [256], [0, 256])
hist_rojo = cv2.calcHist([imagen], [2], None, [256], [0, 256])

# Graficar
plt.figure(figsize=(10, 5))

plt.plot(hist_azul, color='blue', label='Azul')
plt.plot(hist_verde, color='green', label='Verde')
plt.plot(hist_rojo, color='red', label='Rojo')

plt.title("Histogramas de los canales BGR")
plt.xlabel("Intensidad del píxel (0-255)")
plt.ylabel("Cantidad de píxeles")
plt.legend()

plt.show()