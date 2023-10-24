import cv2
import numpy as np 
#carregando a imagem e a convertendo para o espaço de cor HSV
img = cv2.imread('image.jpg')#aqui lê a imagem
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)# aqui converte com a função cvt,
#definindo os alcances da cor
alcance_minimoAzul = (78,158,124)
alcance_maximoAzul = (138,255,255)
mask = cv2.inRange(hsv_img,alcance_minimoAzul,alcance_maximoAzul)
color_image = cv2.bitwise_and(img, img, mask=mask)
#Mostrar cor da imagem
cv2.imshow('Coloured Image', color_image)
cv2.waitKey(0)
cv2.destroyAllWindows()