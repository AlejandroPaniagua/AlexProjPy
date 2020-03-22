''' Multiplicación de
    dos matrices cuadradas '''
# INICIO
''' Inicialización de las matrices '''
A = [[3,2,1],[-1,-3,0],[5,7,8]]
B = [[9,0,1],[-1,7,1],[6,4,1]]
R = [[0,0,0],[0,0,0],[0,0,0]]   # se inicializa la matriz resultado
''' Bucle de multiplicación '''
for k in range(len(A)):
    for j in range(len(B)):
        for t in range(len(B[0])):  # obtención de la sumatoria
            R[k][j] += A[k][t]*B[t][j] ''' en python windows dá error '''
print(R)
# FIN
