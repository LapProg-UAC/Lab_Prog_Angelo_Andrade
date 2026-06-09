import numpy as np
import matplotlib.pyplot as plt

"""
Gera um gráfico da função seno no intervalo [0, 2π] usando NumPy e Matplotlib,
e guarda a imagem como ficheiro PNG.
"""

x = np.linspace(0,2*np.pi,400)    
y = np.sin(x)                      

plt.plot(x,y)                    
plt.savefig("seno.png", dpi=300, bbox_inches='tight')
plt.show()



