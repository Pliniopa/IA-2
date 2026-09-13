import cv2

a = 3
img = r"./Actividades/Codigos/Muestra.png"
imagen = cv2.imread(img, cv2.IMREAD_GRAYSCALE)

sobel_x = cv2.Sobel(imagen, cv2.CV_64F, 1, 0, ksize=a)
sobel_y = cv2.Sobel(imagen, cv2.CV_64F, 0, 1, ksize=a)

sobel_x_abs = cv2.convertScaleAbs(sobel_x)
sobel_y_abs = cv2.convertScaleAbs(sobel_y)

bordes_canny = cv2.Canny(imagen, 50, 150)