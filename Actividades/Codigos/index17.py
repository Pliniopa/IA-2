import cv2

# 1. Cargar la imagen desde tu archivo local
# Asegúrate de colocar el archivo en la misma carpeta o indicar su ruta (ej: 'mi_imagen.jpg')
imagen_original = cv2.imread('./Actividades/Codigos/img-prueba.jpg')

# Verificar que la imagen se haya cargado correctamente
if imagen_original is None:
    print("Error: No se pudo cargar la imagen. Revisa el nombre o la ruta del archivo.")
else:
    # 2. Aplicar los tres filtros con un kernel de 7x7
    kernel_size = 25

    # Filtro de Media (Averaging)
    filtro_media = cv2.blur(imagen_original, (kernel_size, kernel_size))

    # Filtro Gaussiano
    filtro_gaussiano = cv2.GaussianBlur(imagen_original, (kernel_size, kernel_size), 0)

    # Filtro de Mediana
    filtro_mediana = cv2.medianBlur(imagen_original, kernel_size)

    # 3. Mostrar los resultados en ventanas separadas
    cv2.imshow('Original con Ruido', imagen_original)
    cv2.imshow('Filtro de Media (7x7)', filtro_media)
    cv2.imshow('Filtro Gaussiano (7x7)', filtro_gaussiano)
    cv2.imshow('Filtro de Mediana (7x7)', filtro_mediana)

    # Esperar a que se presione una tecla para cerrar las ventanas
    cv2.waitKey(0)
    cv2.destroyAllWindows()