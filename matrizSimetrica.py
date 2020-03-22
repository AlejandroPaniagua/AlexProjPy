''' Generación de una
    matriz simetrica
    de 4x4 '''
# INICIO
import random

n = int(input("Introduce la dimensión de la matriz : "))

''' Generación de la matriz
    resultado por comprension
    de n x n de enteros aleatorios'''
A_simetrica = [[None for k in range(n)] for j in range(n)]
for k in range(n):
    for j in range(n):
        A_simetrica[k][j] = random.randint(0,10) #generación de los numeros
                                                 #aleatorios entre 0 y 10
''' Generación de la matriz simetrica '''
for k in range(n):
    for j in range(k):
        A_simetrica[j][k] = A_simetrica[k][j]
''' Exposición de la matriz simetrica '''
for linea in A_simetrica:
    print(linea) #se imprime en forma de matriz
#FIN

