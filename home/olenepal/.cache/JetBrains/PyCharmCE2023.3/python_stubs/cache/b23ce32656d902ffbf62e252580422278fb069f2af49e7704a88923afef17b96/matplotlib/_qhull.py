# encoding: utf-8
# module matplotlib._qhull calls itself qhull
# from /home/olenepal/.local/lib/python3.10/site-packages/matplotlib/_qhull.cpython-310-x86_64-linux-gnu.so
# by generator 1.147
""" Computing Delaunay triangulations. """
# no imports

# functions

def delaunay(*args, **kwargs): # real signature unknown
    """
    Compute a Delaunay triangulation.
    
    Parameters
    ----------
    x, y : 1d arrays
        The coordinates of the point set, which must consist of at least
        three unique points.
    verbose : int
        Python's verbosity level.
    
    Returns
    -------
    triangles, neighbors : int arrays, shape (ntri, 3)
        Indices of triangle vertices and indices of triangle neighbors.
    """
    pass

def version(*args, **kwargs): # real signature unknown
    """ Return the qhull version string. """
    pass

# no classes
# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x7fd3047ce110>'

__spec__ = None # (!) real value is "ModuleSpec(name='matplotlib._qhull', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x7fd3047ce110>, origin='/home/olenepal/.local/lib/python3.10/site-packages/matplotlib/_qhull.cpython-310-x86_64-linux-gnu.so')"

