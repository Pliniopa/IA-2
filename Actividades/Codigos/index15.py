import cv2
import numpy as np

imagen = r"celula-prueba.jpg"

imagen_p = cv2.imread(imagen)


blur_media = cv2.blur(imagen_p, (5, 5)) 

blur_glass = cv2.GaussianBlur(imagen_p, (5 ,5), 0)

blur_media2 = cv2.medianBlur(imagen_p , 5)

print(blur_media, "\n*********", blur_glass, "\n***********", blur_media2)


