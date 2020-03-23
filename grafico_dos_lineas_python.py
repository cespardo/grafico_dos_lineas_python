import math
import matplotlib.pyplot as plt


#Creo la lista 1 con 8 datos
lista1 = [11,2,3,15,8,13,21,34]
#Creo la lista 2 con 8 datos
lista2 = [2,3,4,2,3,6,4,10]

plt.xlabel("abscisa")   # Inserta el título del eje X 
plt.ylabel("ordenada")   # Inserta el título del eje Y

#Activo el modo interactivo de dibujo


plt.plot(lista1)   # Dibuja el gráfico
plt.plot(lista2)   # No dibuja datos de lista2
plt.show()