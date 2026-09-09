import cv2
import numpy as np

imagen_binaria = np.array([
    [0, 1, 0],
    [1, 1, 1],
    [0, 1, 0],

], dtype=np.uint8)

kernel = np.ones((5, 5), np.uint8)

imagen_ero = cv2.erode(imagen_binaria, kernel, iterations=1)

imagen_dil = cv2.dilate(imagen_binaria, kernel, iterations=1)
print(imagen_binaria)
print("")
print(imagen_ero)
print("")
print(imagen_dil)
