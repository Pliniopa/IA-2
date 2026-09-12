import cv2
import numpy as np

# 1. Generar imagen sintética e incorporar ruido de Sal y Pimienta
width, height = 400, 400
img = np.full((height, width), 128, dtype=np.uint8)  # Fondo gris base

# Añadir ruido aleatorio (5% de la imagen)
amount = 0.05
noisy_img = img.copy()

# Sal (píxeles blancos: 255)
num_salt = np.ceil(amount * img.size * 0.5)
coords = [np.random.randint(0, i - 1, int(num_salt)) for i in img.shape]
noisy_img[tuple(coords)] = 255

# Pimienta (píxeles negros: 0)
num_pepper = np.ceil(amount * img.size * 0.5)
coords = [np.random.randint(0, i - 1, int(num_pepper)) for i in img.shape]
noisy_img[tuple(coords)] = 0

# 2. Aplicar los tres filtros con un kernel agresivo de 7x7
ksize = (7, 7)

# Filtro de Media (Average/Blur)
media_img = cv2.blur(noisy_img, ksize)

# Filtro Gaussiano
gauss_img = cv2.GaussianBlur(noisy_img, ksize, sigmaX=0)

# Filtro de Mediana
mediana_img = cv2.medianBlur(noisy_img, 7)

# 3. Mostrar la imagen con ruido y los tres resultados
cv2.imshow("Original con Ruido Sal y Pimienta", noisy_img)
cv2.imshow("Filtro de Media (7x7)", media_img)
cv2.imshow("Filtro Gaussiano (7x7)", gauss_img)
cv2.imshow("Filtro de Mediana (7x7)", mediana_img)

cv2.waitKey(0)
cv2.destroyAllWindows()