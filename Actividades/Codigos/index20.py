import cv2
import matplotlib.pyplot as plt
import numpy as np

# 1. Cargar la imagen en escala de grises
# Reemplaza 'tu_imagen.jpg' por la ruta de tu archivo
img_path = './Actividades/Codigos/Muestra.png'
image = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

# Si no tienes imagen local, se genera una sintética con geometrías y texturas
if image is None:
    image = np.zeros((400, 400), dtype=np.uint8)
    cv2.rectangle(image, (50, 50), (180, 350), 200, -1)  # Edificio 1
    cv2.rectangle(image, (220, 150), (350, 350), 150, -1) # Edificio 2
    cv2.circle(image, (300, 70), 40, 255, -1)            # Sol/Forma circular
    # Textura simulada (ruido/líneas finas)
    noise = np.random.randint(0, 50, (400, 400), dtype=np.uint8)
    image = cv2.add(image, noise)

# Aplicar un suavizado gaussiano leve para reducir el ruido antes de Sobel/Canny
blurred = cv2.GaussianBlur(image, (3, 3), 0)

# 2. Generar las tres variables
# Sobel X (detecta bordes verticales)
sobel_x = cv2.Sobel(blurred, cv2.CV_64F, 1, 0, ksize=3)
sobel_x = cv2.convertScaleAbs(sobel_x)

# Sobel Y (detecta bordes horizontales)
sobel_y = cv2.Sobel(blurred, cv2.CV_64F, 0, 1, ksize=3)
sobel_y = cv2.convertScaleAbs(sobel_y)

# Algoritmo de Canny (umbrales estándar por defecto)
canny_default = cv2.Canny(blurred, threshold1=100, threshold2=200)

# 3. Panel de visualización principal
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
axes[0, 0].imshow(image, cmap='gray')
axes[0, 0].set_title('Imagen Original')

axes[0, 1].imshow(sobel_x, cmap='gray')
axes[0, 1].set_title('Bordes Verticales (Sobel X)')

axes[1, 0].imshow(sobel_y, cmap='gray')
axes[1, 0].set_title('Bordes Horizontales (Sobel Y)')

axes[1, 1].imshow(canny_default, cmap='gray')
axes[1, 1].set_title('Bordes Combinados (Canny: 100/200)')

for ax in axes.ravel():
    ax.axis('off')
plt.tight_layout()
plt.show()

# 4. Experimentación con Umbrales de Canny
canny_low = cv2.Canny(blurred, threshold1=10, threshold2=50)
canny_high = cv2.Canny(blurred, threshold1=200, threshold2=250)

fig_exp, axes_exp = plt.subplots(1, 3, figsize=(15, 5))
axes_exp[0].imshow(canny_low, cmap='gray')
axes_exp[0].set_title('Umbrales Bajes (10, 50)\n[Mucho Ruido/Textura]')

axes_exp[1].imshow(canny_default, cmap='gray')
axes_exp[1].set_title('Umbrales Medios (100, 200)\n[Balance Optimo]')

axes_exp[2].imshow(canny_high, cmap='gray')
axes_exp[2].set_title('Umbrales Altos (200, 250)\n[Solo Contornos Fuertes]')

for ax in axes_exp:
    ax.axis('off')
plt.tight_layout()
plt.show()