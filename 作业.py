import matplotlib.pyplot as plt
import numpy as np

x = np.linspace (-np.pi/2, np.pi, num = 256, endpoint=True)
T, C = np.tan(x), 1/np.tan(x)
fig,ax = plt.subplots(1,2)
ax[0].plot(x,T, color = "r", linewidth = 2, linestyle= "-", label = "tan")
ax[1].plot(x,C, color = "b", linewidth = 2, linestyle = "-", label = "cot")

for i in range(2):
    ax[i].spines['right'].set_color('none')
    ax[i].spines['top'].set_color('none')
    ax[i].xaxis.set_ticks_position('bottom')
    ax[i].spines['bottom'].set_position(('data',0))
    ax[i].yaxis.set_ticks_position('left')
    ax[i].spines['left'].set_position(('data',0))

ax[0].set_xlim(-np.pi/2,+np.pi/2)
ax[0].set_ylim(-3,3)
ax[0].set_xticks([-np.pi/2,0, np.pi/2],[r'$-\pi/2$',r'$0$',r'$+\pi/2$'])
ax[0].set_yticks([-3,-2,-1,0,1,2,3])
ax[0].legend(loc='upper left',frameon = True)
ax[1].set_xlim(0,+np.pi)
ax[1].set_ylim(-3,3)
ax[1].set_xticks([0, np.pi/2, np.pi],[r'$0$',r'$+\pi/2$',r'$+\pi$'])
ax[1].set_yticks([-3,-2,-1,0,1,2,3])
ax[1].legend(loc='upper right',frameon = True)

plt.show()



