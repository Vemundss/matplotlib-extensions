# Matplotlib-extensions

Repository extending standard matplotlib functionality (typically) to higher dimensions with convenient and intuitive APIs. Higher dimensions can mean e.g. including time, color or multiple figure axes.

Extended functions:

### _time_scatter_
time_scatter extends plt.scatter(x, y, OPTIONAL: z) to accept temporally dependent spatial samples x(t), y(t), OPTIONAL: z(t) and animates it. The arguments to time_scatter, thus, has shape shape(x(t)) = (N,T), compared to the purely spatial samples of scatter with shape shape(x) = (N,).

```python
import numpy as np
from sklearn.datasets import make_swiss_roll
# sample some data (shape: (200,2))
data = make_swiss_roll(200, noise=0.1)[0][:, [0, 2]]
# sort data based on radial distance to origin
idxs = np.argsort(np.linalg.norm(data, axis=1))
data = data[idxs]

# Regular 2D scatter plot of data
fig, ax = plt.subplots(figsize=(3,3))
ax.scatter(*data.T, alpha=0.2)

# Plot the same data, but over time using time_scatter
# the shape of data.T[:,None] is (2,1,200)
# meaning we display each sample at distinct timepoints
from mplextensions import time_scatter
html = time_scatter(*data.T[:,None], fps=24, fig=fig, ax=ax)
html # show animation a notebook
```

![swiss_role_gif](https://github.com/user-attachments/assets/a8f0ba54-516b-4eaa-a9a4-587a99a353f8)


### _multi_imshow_
extends matplotlib's _imshow_ plotting many images on a square grid. Simply send a tensor **zz** of dimensions (Nimages, H, W) which contains Nimages with height H and width W. Calling the function as: **multiimshow(zz)** will plot all the images on a square grid.

