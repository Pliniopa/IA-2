import cv2
import numpy as np

matriz = np.array([
    [80, 120, 140],
    [90, 200, 210],
    [50, 130, 250]
], dtype=np.uint8)

T = 100

img, imagen_binaria = cv2.threshold(matriz, T, 255, cv2.THRESH_BINARY)

print(imagen_binaria)