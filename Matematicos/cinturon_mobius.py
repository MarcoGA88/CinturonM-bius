import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

u=np.linspace(0, 2*np.pi,100)
v=np.linspace(-1,1,20)
u,v = np.meshgrid(u,v)

x=np.cos(u)*(1+(v/2)*np.cos(u/2))
y=np.sin(u)*(1+(v/2)*np.cos(u/2))
z=(v/2)*np.sin(u/2)


# Gráfico 3D
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z, color='grey', edgecolor='k', alpha=1)


# Configuración del gráfico
ax.set_title("Cinturón de Möbius", fontsize=14)
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

#Inicializacon del punto movil (Entidad)
point,=ax.plot([],[],[], 'ro', markersize=8)

def update(frame):
    u_pos = 2*np.pi * frame/100 
    v_pos = 0

    x_pos=x=np.cos(u_pos)*(1+(v_pos/2)*np.cos(u_pos/2))
    y_pos=np.sin(u_pos)*(1+(v_pos/2)*np.cos(u_pos/2))
    z_pos=(v_pos/2)*np.sin(u_pos/2)

    point.set_data([x_pos],[y_pos])
    point.set_3d_properties([z_pos])
    return point,

ani=FuncAnimation(fig,update,frames=100, interval=100, blit=True)

plt.show()