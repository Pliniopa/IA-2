import cv2

# Declaración y carga de imágenes
imagen_color = cv2.imread('./Actividades/Codigos/Muestra.png')
imagen_gris = cv2.cvtColor(imagen_color, cv2.COLOR_BGR2GRAY)
_, imagen_binaria = cv2.threshold(imagen_gris, 127, 255, cv2.THRESH_BINARY)

# Tu código original
contornos, jewrarquia = cv2.findContours(imagen_binaria, 
                                         cv2.RETR_EXTERNAL, 
                                         cv2.CHAIN_APPROX_SIMPLE)

for cnt in contornos:
    area = cv2.contourArea(cnt)
    if area > 500:
        x, y, w, h = cv2.boundingRect(cnt)

        cv2.rectangle(imagen_color,(x,y),(x + w, y + h),(0, 255, 0),2)

        M = cv2.moments(cnt)
        if M["M00"] != 0:
            cx = int(M["m10"] / M["m00"])
            cy = int(M["m01"] / M["m00"])
            cv2.circle(imagen_color, (cx, cy), 5, (0,0,255), -1)

cv2.imshow("analisis de objetos", imagen_color)
cv2.waitKey(0)
cv2.destroyAllWindows()