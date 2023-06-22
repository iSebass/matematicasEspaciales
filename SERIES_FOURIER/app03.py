#Serie de Fourier para una onda cuadrada
'''

    f(x) = 4/pi   sumatoria(1/n  * sin (n pi x/L) )

    con valores de n impar
'''

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from celluloid import Camera


#plt.style.use('seaborn')

def funcion_Onda_cuadrada(x, n):
    m = 2*n-1
    f = (4/np.pi)*(1/m)*np.sin(m*np.pi*x/L)
    return f


fig = plt.figure()
camera = Camera(fig)

L = np.pi
ciclos = 1
x = np.linspace(-0.0001, 2*ciclos*L, 1000)
f = 0
n = 1
n_total = 50

while n<n_total:
    
    f += funcion_Onda_cuadrada(x,n)
    '''
    plt.plot(x,f,label="n= {}".format(2*n-1))
    '''
    plt.plot(x,f,c='tab:red')
    camera.snap()
    n += 1


#plt.plot(x, signal.square(x), color='k')
animation = camera.animate()
animation.save('fourier.gif')

'''
plt.legend()
plt.show()
'''
