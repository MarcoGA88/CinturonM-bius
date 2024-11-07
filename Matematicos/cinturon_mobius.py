import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

u=np.linspace(0, 2*np.pi)
v=np.linspace(-1,1)

u,v = np.meshgrid(u,v)

x=np.cos(u)*(1+(v/2)*np.cos(u/2))
y=np.sin(u)*(1+(v/2)*np.cos(u/2))
z=(v/2)*np.sin(u/2)


# Gráfico 3D
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z, color='cyan', edgecolor='k', alpha=0.8)

# Configuración del gráfico
ax.set_title("Cinturón de Möbius", fontsize=14)
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

plt.show()