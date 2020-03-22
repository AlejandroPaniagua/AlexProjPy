''' Obtención de la matriz
    identidad de 4 x 4 '''
#INICIO
''' Generación de la matriz de ceros '''
I = [[0 for k in range (4)] for j in range (4)]

''' Generación de los elementos de la
    diagonal principal transformandolos
    en unos '''
for k in range(4):
    I[k][k] = 1

''' Despliegue de la matriz identidad '''
for k in range(4):
    print()  # salto de linea
    for j in range(4):
        print(I[k][j],end=", ")
#FIN
