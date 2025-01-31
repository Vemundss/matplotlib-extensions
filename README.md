# Matplotlib-extensions

Extends standard matplotlib plotting functions to higher dimensions with convenient and intuitive APIs. Higher dimensions can mean e.g. including time, color or multiple figure axes.

Extended functions:

### _time_scatter_
time_scatter extends plt.scatter(x, y, OPTIONAL: z) to accept temporally dependent spatial samples x(t), y(t), OPTIONAL: z(t) and animates it. The arguments to time_scatter, thus, has shape shape(x(t)) = (N,T), compared to the purely spatial samples of scatter with shape shape(x) = (N,).

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_swiss_roll
# sample some data (shape: (200,2))
data = make_swiss_roll(200, noise=0)[0][:, [0, 2]]
# sort data based on radial distance to origin
idxs = np.argsort(np.linalg.norm(data, axis=1))
data = data[idxs]

# Regular 2D scatter plot of data
fig, ax = plt.subplots()
ax.scatter(*data.T, alpha=0.2)

# Plot the same data, but over time using time_scatter
# the shape of data.T[:,None] is (2,1,200)
# meaning we display each sample at distinct timepoints
from mplextensions import time_scatter
time_scatter(*data.T[:,None], fps=24, fig=fig, ax=ax)
```

<div align="center">
    <img src="https://github.com/user-attachments/assets/66467ae5-3b4b-4794-8a26-3c9bde07796c" width="400">
</div>


### _time_plot_
time_plot extends plt.plot(x, y, OPTIONAL: z) to accept temporally dependent spatial samples x(t), y(t), OPTIONAL: z(t) and animates it. The arguments to time_plot, thus, has shape shape(x(t)) = (N,T), compared to the purely spatial samples of scatter with shape shape(x) = (N,).

```python
import numpy as np
from mplextensions import time_plot

# Create a 2D sine wave
T = 100
x = np.linspace(0, 2 * np.pi, 200) # N=200
x_2d = np.tile(x[:, np.newaxis], (1, T))  # Shape: (N, T)
t_values = np.linspace(0, 2 * np.pi, T)
y_2d = np.sin(x_2d + t_values)  # Shape: (N, T)

time_plot(x_2d, y_2d)
```

<div align="center">
    <img src="https://github.com/user-attachments/assets/42006394-e286-49d7-8dd9-93f7aa450dc7" width="400">
</div>



### _multi_imshow_
multi_imshow extends plt.imshow(X) to accept 3D images and shows the slices of the first dimension on a 2D grid. The argument X has shape (N, H, W) or (N, H, W, C). number of images, height, width, and optionally channels.

```python
import numpy as np
from mplextensions import multi_imshow

# create some 3D data
mesh = np.stack(np.meshgrid(*[np.linspace(-np.pi, np.pi, 32)]*3), axis=-1) # Shape: (32, 32, 32, 3)
mesh = np.exp(-np.linalg.norm(mesh, axis=-1)) # Shape: (32, 32, 32) => 3D Gaussian in (T, X, Y)

multi_imshow(mesh)
```

<div align="center">
    <img src="https://github.com/user-attachments/assets/b19cad8b-0ab7-4bc7-af71-3f11e232bf1e" width="400">
</div>



### _time_imshow_
time_imshow extends plt.imshow(X) to accept 3D images and animates it along the first dimension. The argument X to time_imshow, thus, has shape (T, H, W) or (T, H, W, C). Time, height, width, and optionally channels.

```python
import numpy as np
from mplextensions import time_imshow

# create some 3D data
mesh = np.stack(np.meshgrid(*[np.linspace(-np.pi, np.pi, 32)]*3), axis=-1) # Shape: (32, 32, 32, 3)
mesh = np.exp(-np.linalg.norm(mesh, axis=-1)) # Shape: (32, 32, 32) => 3D Gaussian in (T, X, Y)

time_imshow(mesh, add_colorbar=True)
```

<div align="center">
    <img src="https://github.com/user-attachments/assets/2a443d14-d84d-422e-8631-56698dc1110c" width="400">
</div>



### _multicolor_plot_
multicolor_plot extends plt.plot(X) to accept a "values" parameter which colors the plot continuously.

```python
import numpy as np
from mplextensions import multicolor_plot

x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)
values = y

multicolor_plot(x, y)
```

<div align="center">
    <img src="https://github.com/user-attachments/assets/4b2c54d3-a533-4c94-b596-a31fc77b6314" width="400">
</div>
