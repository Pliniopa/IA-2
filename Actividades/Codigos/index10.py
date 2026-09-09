import cv2

ruta_img = "Actividades/Codigos/Muestra.png"

imagen = cv2.imread(ruta_img, cv2.IMREAD_GRAYSCALE)

imagen_binaria = cv2.threshold(imagen, 127, 255, cv2.THRESH_BINARY)

T_ostu, imagen_ostu = cv2.threshold(imagen, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

print (f"El umbral optimo es {T_ostu}")

