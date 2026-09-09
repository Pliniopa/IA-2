import cv2
import numpy as np

img = f"Actividades\Codigos\celula-prueba.jpg"

# Cargar imagen
imagen = cv2.imread(img, cv2.IMREAD_GRAYSCALE)

# Binarización
_, binaria = cv2.threshold(imagen, 127, 255, cv2.THRESH_BINARY)

# Elemento estructurante 3x3
kernel = np.ones((3,3), np.uint8)

# Apertura = Erosión + Dilatación
apertura = cv2.erode(binaria, kernel)
apertura = cv2.dilate(apertura, kernel)

# Cierre = Dilatación + Erosión
cierre = cv2.dilate(binaria, kernel)
cierre = cv2.erode(cierre, kernel)

# Mostrar resultados
cv2.imshow("Original binarizada", binaria)
cv2.imshow("Apertura", apertura)
cv2.imshow("Cierre", cierre)

cv2.waitKey(0)
cv2.destroyAllWindows()