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

![image](https://github.com/user-attachments/assets/0d1c15d2-aa34-4cc0-bc01-bc8c2208268b)


### _time_plot_
time_plot extends plt.plot(x, y, OPTIONAL: z) to accept temporally dependent spatial samples x(t), y(t), OPTIONAL: z(t) and animates it. The arguments to time_plot, thus, has shape shape(x(t)) = (N,T), compared to the purely spatial samples of scatter with shape shape(x) = (N,).

```python
import numpy as np
from mplextensions.plotting_functions import time_plot

# Create a 2D sine wave
T = 100
x = np.linspace(0, 2 * np.pi, 200) # N=200
x_2d = np.tile(x[:, np.newaxis], (1, T))  # Shape: (N, T)
t_values = np.linspace(0, 2 * np.pi, T)
y_2d = np.sin(x_2d + t_values)  # Shape: (N, T)

time_plot(x_2d, y_2d)
```

![image](https://github.com/user-attachments/assets/6224d9cf-488d-4f4b-8830-03d7610e4a68)

