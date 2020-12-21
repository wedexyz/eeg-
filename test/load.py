

import numpy as np
import matplotlib.pyplot as plt

d = np.load("data_baru\\idle\\1604315006.npy")

fig, (ax1, ax2) = plt.subplots(1, 2)
fig.suptitle('Horizontally stacked subplots')
ax1.plot(d[0][16])
ax2.plot(d[200])
plt.show()