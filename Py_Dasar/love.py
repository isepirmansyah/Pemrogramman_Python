import matplotlib.pylab as plt
import numpy as np

x = np.linspace(-2,2,1000)
y1 = np.sqrt(1-(abs(x)-1)**2)
y2 = -3*np.sqrt(1-(abs(x)/2)**0.5)
plt.fill_between(x, y1, color='pink')
plt.fill_between(x, y2, color='pink')
plt.xlim([-2.5, 2.5])
plt.ylim([-3.5, 1.5])
plt.text(0, -0.4, 'Anggi & Irmansyah', fontsize=20, fontweight='bold',
           color='blue', horizontalalignment='center')
plt.text(0, -0.8, 'Wedding', fontsize=10, fontweight='normal',
           color='green', horizontalalignment='center')
plt.show()