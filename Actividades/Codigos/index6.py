import cv2
import numpy as np

imagen = cv2.imread(r"\Muestra.png")

canal_azul = imagen[:, :, 0]
canal_verde = imagen[:, :, 1]
canal_rojo = imagen[:, :, 2]

imagen_solo_roja = np.copy(imagen)
imagen_solo_roja[:, :, 0] = 2
imagen_solo_roja[:, :, 1] = 2

cv2.imshow("Imagen", imagen_solo_roja)
cv2.waitKey(0)
cv2.destroyAllWindows()