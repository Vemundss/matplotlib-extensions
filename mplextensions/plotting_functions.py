import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, ArtistAnimation
from IPython.display import HTML
from mpl_toolkits.axes_grid1 import ImageGrid
from matplotlib.collections import LineCollection
from matplotlib.colors import Normalize


def time_imshow(X, fig=None, ax=None, fps=None, return_fig=False, interval=50, add_colorbar=False, **kwargs):
    """
    Extends matplotlib imshow to 3D images and considers the first dimension as time by displaying it
    as an animation.
    
    Parameters
    ----------
    X : np.ndarray
        3D array of shape (T, H, W) or (T, H, W, C)
    fig : matplotlib.figure.Figure, optional
        Figure to use for the animation, by default None
    ax : matplotlib.axes.Axes, optional
        Axes to use for the animation, by default None
    fps : int, optional
        Frames per second for the animation, by default None
    return_fig : bool, optional
        Whether to return the figure and axes, by default False
    interval : int, optional
        Interval between frames in milliseconds, by default 50
    add_colorbar : bool, optional
        Whether to add a colorbar to the plot, by default False
    **kwargs : dict
        Additional keyword arguments to pass to the `imshow` function.

    Returns
    -------
    HTML
        HTML object displaying the animation.
    """
    # Validate input shape
    if X.ndim not in (3, 4):
        raise ValueError("Input array X must have 3 or 4 dimensions (T, H, W) or (T, H, W, C).")

    # Create figure and axes if not provided
    if fig is None or ax is None:
        fig, ax = plt.subplots()

    # Determine the number of frames (T) and prepare color normalization
    T = X.shape[0]
    vmin, vmax = X.min(), X.max()
    kwargs.setdefault('vmin', vmin)
    kwargs.setdefault('vmax', vmax)
    
    artists = []
    # Plot frames
    for t in range(T):
        img = ax.imshow(X[t], **kwargs)
        artists.append([img])

    # Add colorbar if required
    if add_colorbar:
        sm = plt.cm.ScalarMappable(cmap=kwargs.get('cmap', 'viridis'), norm=Normalize(vmin=vmin, vmax=vmax))
        fig.colorbar(sm, ax=ax)

    # Calculate interval if fps is provided
    interval = 1000 / fps if fps else interval
    # Create the animation
    animation = ArtistAnimation(fig, artists, interval=interval)
    # Return animation
    html = HTML(animation.to_jshtml())
    if return_fig:
        return html, fig, ax, animation
    plt.close(fig)
    return html


def time_plot(*args, fig=None, ax=None, figsize=(3,3), fps=None, interval=50, **kwargs):
    """
    Extends matplotlib.pyplot.plot to include a time dimension (T) for each array
    which is animated to show the evolution of the data over time.

    Simply put, this function is a wrapper around matplotlib.animation.FuncAnimation
    that animates a line plot.

    The goal is to make it easier to visualize the evolution of data over time,
    through a simple and intuitive API: time_plot(x, y, OPTIONAL: z), where x, y, and z
    are numpy arrays with the same shape, except for the last dimension which should be T or 1.
    I.e., for a 2 or 3D line plot, x and y (and z) should have shape (N, T) or (N, 1), 
    where N is the number of points.

    For multiple lines, simply include an additional dimension for the number of lines, 
    e.g. (N, L, T) or (N, L, 1) for L lines.
    
    Parameters
    ----------
    args : list of np.ndarray
        List of arrays to plot. The last dimension of each array should be either T or 1.
    fig : matplotlib.figure.Figure, optional
        Figure to plot on.
    ax : matplotlib.axes.Axes, optional
        Axes to plot on.
    fps : int, optional
        Frames per second for the animation.
    interval : int, optional
        Interval between frames in milliseconds.
    **kwargs :
        Additional keyword arguments for the plot function.
    
    Returns
    -------
    html : IPython.display.HTML
        The HTML object to display the animation in Jupyter Notebook.
    fig : matplotlib.figure.Figure
        The figure object.
    ax : matplotlib.axes.Axes
        The axes object.
    animation : matplotlib.animation.FuncAnimation
        The animation object.
    
    Examples
    --------
    # Create a 2D sine wave
    frames = 100
    x = np.linspace(0, 2 * np.pi, 200)
    x_2d = np.tile(x[:, np.newaxis], (1, frames))  # Shape: (200, frames)
    t_values = np.linspace(0, 2 * np.pi, frames)
    y_2d = np.sin(x_2d + t_values)  # Shape: (200, frames)
    
    fig, ax, animation, html = time_plot(x_2d, y_2d)
    plt.close(fig)  # Close the figure to prevent it from being displayed
    html  # Display the animation in Jupyter Notebook
    """
    # Create figure and axes if not provided
    if fig is None or ax is None:
        if len(args) == 3:
            fig = plt.figure(figsize=figsize)
            ax = fig.add_subplot(111, projection='3d')
        else:
            fig, ax = plt.subplots(figsize=figsize)

    # Ensure all args are numpy arrays
    args = [np.array(arg) for arg in args]
    # Determine the number of frames (T)
    T = max(arg.shape[-1] for arg in args)
    # Plot the initial frame (t=0)
    line, = ax.plot(*[arg[...,0] for arg in args], **kwargs)
    # Set limits to data range
    xmin, xmax = args[0].min(), args[0].max()
    ymin, ymax = args[1].min(), args[1].max()
    ax.set_xlim(xmin, xmax)
    ax.set_ylim(ymin, ymax)
    if len(args) == 3:
        zmin, zmax = args[2].min(), args[2].max()
        ax.set_zlim(zmin, zmax)

    def animate(t):
        t = t % T  # Loop over frames
        line.set_data(args[0][..., t], args[1][..., t])
        if len(args) == 3:
            line.set_3d_properties(args[2][..., t])
        return line,

    # Calculate interval if fps is provided
    interval = 1000 / fps if fps else interval
    # Create the animation
    animation = FuncAnimation(fig, animate, frames=T, interval=interval, blit=True)
    html = HTML(animation.to_jshtml())
    return html, fig, ax, animation


def time_scatter(*args, fig=None, ax=None, fps=None, return_fig=False, interval=50, **kwargs):
    """
    Extends matplotlib.pyplot.scatter to include a time dimension (T) for each array
    which is animated to show the evolution of the data over time.
    
    Parameters
    ----------
    args : list of np.ndarray
        List of arrays to plot. The last dimension of each array should be either T or 1.
    fig : matplotlib.figure.Figure, optional
        Figure to plot on.
    ax : matplotlib.axes.Axes, optional
        Axes to plot on.
    fps : int, optional
        Frames per second for the animation.
    interval : int, optional
        Interval between frames in milliseconds.
    **kwargs :
        Additional keyword arguments for the scatter function.
    
    Returns
    -------
    html : IPython.display.HTML
        The HTML object to display the animation in Jupyter Notebook.
    fig : matplotlib.figure.Figure
        The figure object.
    ax : matplotlib.axes.Axes
        The axes object.
    animation : matplotlib.animation.FuncAnimation
        The animation object.
    """
    # Create figure and axes if not provided
    if fig is None or ax is None:
        if len(args) == 3:
            fig = plt.figure()
            ax = fig.add_subplot(111, projection='3d')
        else:
            fig, ax = plt.subplots()
    # Ensure all args are numpy arrays
    args = [np.array(arg) for arg in args]
    # Determine the number of frames (T)
    T = max(arg.shape[-1] for arg in args)
    # plot frames
    artists = []
    for t in range(T):
        scatter = ax.scatter(*[arg[...,t] for arg in args], **kwargs)
        artists.append([scatter])
    # Calculate interval if fps is provided
    interval = 1000 / fps if fps else interval
    # Create the animation
    animation = ArtistAnimation(fig, artists, interval=interval)
    #return animation
    html = HTML(animation.to_jshtml())
    if return_fig:
        return html, fig, ax, animation
    plt.close(fig)
    return html


def multi_imshow(zz, figsize=(10,10), normalize=True, add_colorbar=True, rect=(0, 0, 1, 0.87), axes_pad=0.05, **kwargs):
    """
    Displays multiple images in a grid format.

    Parameters
    ----------
    zz : np.ndarray
        An array of images to display. Must be 3D, with shape (n_images, height, width).
    figsize : tuple, optional
        Size of the figure.
    normalize : bool, optional
        Whether to normalize the color scale.
    add_colorbar : bool, optional
        Whether to add a colorbar.
    rect : tuple, optional
        Position of the grid within the figure.
    axes_pad : float, optional
        Padding between axes.
    **kwargs :
        Additional keyword arguments for imshow.
    """
    # Validate input
    if not isinstance(zz, np.ndarray):
        zz = np.array(zz)
    if zz.ndim != 3:
        raise ValueError("Input 'zz' must be a 3D array with shape (n_images, height, width).")

    n_images = zz.shape[0]
    ncols = int(np.ceil(np.sqrt(n_images)))
    nrows = int(np.ceil(n_images / ncols))

    fig = plt.figure(figsize=figsize)
    grid_kwargs = {
        'rect': rect,
        'nrows_ncols': (nrows, ncols),
        'axes_pad': axes_pad
    }

    if add_colorbar:
        grid_kwargs.update({
            'cbar_mode': 'single',
            'cbar_location': 'right',
            'cbar_pad': 0.1,
            'cbar_size': '5%'
        })

    grid = ImageGrid(fig, **grid_kwargs)

    vmin, vmax = (np.nanmin(zz), np.nanmax(zz)) if normalize else (None, None)

    # Plot images
    im = None
    for ax, data in zip(grid, zz):
        im = ax.imshow(data, vmin=vmin, vmax=vmax, **kwargs)
        ax.axis('off')

    # Add colorbar if required
    if add_colorbar and im is not None:
        fig.colorbar(im, cax=grid.cbar_axes[0])

    return fig, grid.axes_all


def multicolor_plot(rs, values, fig=None, ax=None, cmap='coolwarm', **kwargs):
    """
    Plots a line with varying colors along its length based on `values`.
    
    Parameters
    ----------
    rs : (N, 2) array
        Coordinates of the line.
    values : (N,) array
        Values used to color the line.
    fig : matplotlib.figure.Figure, optional
        Figure to plot on.
    ax : matplotlib.axes.Axes, optional
        Axes to plot on.
    cmap : str or Colormap, optional
        Colormap to use.
    **kwargs :
        Additional keyword arguments for LineCollection.
    """
    if fig is None or ax is None:
        fig, ax = plt.subplots(figsize=(3, 3))
    cmap = plt.get_cmap(cmap)
    norm = Normalize(vmin=values.min(), vmax=values.max())
    # Create segments
    points = rs.reshape(-1, 1, 2)
    segments = np.concatenate([points[:-1], points[1:]], axis=1)
    # Create LineCollection
    lc = LineCollection(segments, array=values[:-1], cmap=cmap, norm=norm, **kwargs)
    ax.add_collection(lc)
    ax.autoscale()
    return fig, ax
