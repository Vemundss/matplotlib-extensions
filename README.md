# Matplotlib-extensions

Repository extending standard matplotlib functionality (typically) to higher dimensions with convenient and intuitive APIs.

Extended functions:
**multi_imshow** extends matplotlib's _imshow_ plotting many images on a square grid. Simply send a tensor **zz** of dimensions (Nimages, H, W) which contains Nimages with height H and width W. Calling the function as: **multiimshow(zz)** will plot all the images on a square grid.

**time_plot**

