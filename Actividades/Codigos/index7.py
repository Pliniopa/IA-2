import numpy as np
import cv2

imagen = r"C:\Test\py\Muestra.png"

def gris_amarillo():
    pixel = np.array([0,255,255])
    gris = (0.114 * pixel[0]) + (0.587 * pixel[1]) + (0.299 * pixel[2])
    print("valor en escala de grises es: ", gris)



def gris_amarillo_opencv():
    pixel = np.array([[[0, 255, 255]]], dtype=np.uint8)
    gris = cv2.cvtColor(pixel, cv2.COLOR_BGR2GRAY)
    print (gris)


def imagen_gris(imagen):
    imagen = cv2.imread(imagen)

    img_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

    cv2.imshow("Imagen Original", imagen)
    cv2.imshow("escala de grises: ", img_gris)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
gris_amarillo()
print("")
gris_amarillo_opencv()
print("")
imagen_gris(imagen)
