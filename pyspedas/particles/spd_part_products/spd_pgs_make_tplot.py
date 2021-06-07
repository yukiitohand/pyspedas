
import numpy as np
from pytplot import store_data, options

def spd_pgs_make_tplot(name, x=None, y=None, z=None, units='', ylog=False, zlog=True, colorbar='jet'):
    """
    Create tplot variable with standard spectrogram settings

    Input:
        name: str
            Name of the new tplot variable to create

    Parameters:
        x: numpy.ndarray
            X-axis values (time)

        y: numpy.ndarray
            Y-axis values

        z: numpy.ndarray
            Z-axis values (data)

        units: str
            Units string to store in the metadata

        ylog: bool
            Set the y-axis to log scale (default: False)

        zlog: bool
            Set the z-axis to log scale (default: True)

        colorbar: str
            PyTplot 'Colormap' option (default: 'jet')

    Returns:
        String containing new variable name

    """

    if not isinstance(x, np.ndarray) or not isinstance(y, np.ndarray) or not isinstance(z, np.ndarray) :
        print('Error, must specify x, y and z parameters')
        return

    store_data(name, data={'x': x, 'y': z, 'v': y})
    options(name, 'ylog', ylog)
    options(name, 'zlog', zlog)
    options(name, 'Spec', True)
    options(name, 'Colormap', colorbar)
    return name