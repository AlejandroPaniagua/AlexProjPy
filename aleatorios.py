''' Generación de números
    aleatorios '''
#INICIO
import random

num = []
for i in range(10):
    n = random.randint(0,20)  # imprimira números enteros entre 0 y 20 incluidos
    num.append(n)
print(num)
''' para imprimir numeros aleatorios en coma flotante enre 0 y 1
    se pone random.random() '''
#FIN
