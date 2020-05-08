''' Este es un programa que crea un gráfico en 3D '''
from pylab import arange , sin , sqrt , meshgrid , figure , cm
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.pyplot import show

fig = figure() # crea una ventana para una figura
ax = Axes3D(fig) # la figura fig se graficará en 3D
X = arange(-4,4,0.25) # crea una lista con estos parametros para el eje X
Y = arange(-4,4,0.25) # crea una lista con estos parametros para el eje Y
X, Y = meshgrid(X, Y) # rejilla para graficar en 3D
R = sqrt(abs(X**3) + Y**2) # raiz del valor absoluto de X al cubo mas Y al cuadrado
Z = sin(R) # obtención del seno de R
ax.plot_surface(X, Y, Z, rstride = 1, cstride = 1, cmap = cm.hot) # grafica superficies
 # el valor de rstride y cstride nos dice el paso entre lineas del dibujo
ax.contourf(X, Y, Z, zdir = 'z' , offset = -2, cmap = cm.hot) # hace grafica de contorno
ax.set_zlim(-2, 2) # coloca los limites de la gráfica en z
show()
