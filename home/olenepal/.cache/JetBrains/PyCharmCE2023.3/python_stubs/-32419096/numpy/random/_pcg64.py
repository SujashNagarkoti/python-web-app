# encoding: utf-8
# module numpy.random._pcg64
# from /home/olenepal/.local/lib/python3.10/site-packages/numpy/random/_pcg64.cpython-310-x86_64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import numpy as np # /home/olenepal/.local/lib/python3.10/site-packages/numpy/__init__.py
import numpy.random.bit_generator as __numpy_random_bit_generator


# no functions
# classes

class PCG64(__numpy_random_bit_generator.BitGenerator):
    """
    PCG64(seed=None)
    
        BitGenerator for the PCG-64 pseudo-random number generator.
    
        Parameters
        ----------
        seed : {None, int, array_like[ints], SeedSequence}, optional
            A seed to initialize the `BitGenerator`. If None, then fresh,
            unpredictable entropy will be pulled from the OS. If an ``int`` or
            ``array_like[ints]`` is passed, then it will be passed to
            `SeedSequence` to derive the initial `BitGenerator` state. One may also
            pass in a `SeedSequence` instance.
    
        Notes
        -----
        PCG-64 is a 128-bit implementation of O'Neill's permutation congruential
        generator ([1]_, [2]_). PCG-64 has a period of :math:`2^{128}` and supports
        advancing an arbitrary number of steps as well as :math:`2^{127}` streams.
        The specific member of the PCG family that we use is PCG XSL RR 128/64
        as described in the paper ([2]_).
    
        ``PCG64`` provides a capsule containing function pointers that produce
        doubles, and unsigned 32 and 64- bit integers. These are not
        directly consumable in Python and must be consumed by a ``Generator``
        or similar object that supports low-level access.
    
        Supports the method :meth:`advance` to advance the RNG an arbitrary number of
        steps. The state of the PCG-64 RNG is represented by 2 128-bit unsigned
        integers.
    
        **State and Seeding**
    
        The ``PCG64`` state vector consists of 2 unsigned 128-bit values,
        which are represented externally as Python ints. One is the state of the
        PRNG, which is advanced by a linear congruential generator (LCG). The
        second is a fixed odd increment used in the LCG.
    
        The input seed is processed by `SeedSequence` to generate both values. The
        increment is not independently settable.
    
        **Parallel Features**
    
        The preferred way to use a BitGenerator in parallel applications is to use
        the `SeedSequence.spawn` method to obtain entropy values, and to use these
        to generate new BitGenerators:
    
        >>> from numpy.random import Generator, PCG64, SeedSequence
        >>> sg = SeedSequence(1234)
        >>> rg = [Generator(PCG64(s)) for s in sg.spawn(10)]
    
        **Compatibility Guarantee**
    
        ``PCG64`` makes a guarantee that a fixed seed will always produce
        the same random integer stream.
    
        References
        ----------
        .. [1] `"PCG, A Family of Better Random Number Generators"
               <http://www.pcg-random.org/>`_
        .. [2] O'Neill, Melissa E. `"PCG: A Family of Simple Fast Space-Efficient
               Statistically Good Algorithms for Random Number Generation"
               <https://www.cs.hmc.edu/tr/hmc-cs-2014-0905.pdf>`_
    """
    def advance(self, delta): # real signature unknown; restored from __doc__
        """
        advance(delta)
        
                Advance the underlying RNG as-if delta draws have occurred.
        
                Parameters
                ----------
                delta : integer, positive
                    Number of draws to advance the RNG. Must be less than the
                    size state variable in the underlying RNG.
        
                Returns
                -------
                self : PCG64
                    RNG advanced delta steps
        
                Notes
                -----
                Advancing a RNG updates the underlying RNG state as-if a given
                number of calls to the underlying RNG have been made. In general
                there is not a one-to-one relationship between the number output
                random values from a particular distribution and the number of
                draws from the core RNG.  This occurs for two reasons:
        
                * The random values are simulated using a rejection-based method
                  and so, on average, more than one value from the underlying
                  RNG is required to generate an single draw.
                * The number of bits required to generate a simulated value
                  differs from the number of bits generated by the underlying
                  RNG.  For example, two 16-bit integer values can be simulated
                  from a single draw of a 32-bit RNG.
        
                Advancing the RNG state resets any pre-computed random numbers.
                This is required to ensure exact reproducibility.
        """
        pass

    def jumped(self, jumps=1): # real signature unknown; restored from __doc__
        """
        jumped(jumps=1)
        
                Returns a new bit generator with the state jumped.
        
                Jumps the state as-if jumps * 210306068529402873165736369884012333109
                random numbers have been generated.
        
                Parameters
                ----------
                jumps : integer, positive
                    Number of times to jump the state of the bit generator returned
        
                Returns
                -------
                bit_generator : PCG64
                    New instance of generator jumped iter times
        
                Notes
                -----
                The step size is phi-1 when multiplied by 2**128 where phi is the
                golden ratio.
        """
        pass

    def __init__(self, seed=None): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce_cython__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate_cython__(self, *args, **kwargs): # real signature unknown
        pass

    state = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Get or set the PRNG state

        Returns
        -------
        state : dict
            Dictionary containing the information required to describe the
            state of the PRNG
        """


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x7fd2ef953060>'


class PCG64DXSM(__numpy_random_bit_generator.BitGenerator):
    """
    PCG64DXSM(seed=None)
    
        BitGenerator for the PCG-64 DXSM pseudo-random number generator.
    
        Parameters
        ----------
        seed : {None, int, array_like[ints], SeedSequence}, optional
            A seed to initialize the `BitGenerator`. If None, then fresh,
            unpredictable entropy will be pulled from the OS. If an ``int`` or
            ``array_like[ints]`` is passed, then it will be passed to
            `SeedSequence` to derive the initial `BitGenerator` state. One may also
            pass in a `SeedSequence` instance.
    
        Notes
        -----
        PCG-64 DXSM is a 128-bit implementation of O'Neill's permutation congruential
        generator ([1]_, [2]_). PCG-64 DXSM has a period of :math:`2^{128}` and supports
        advancing an arbitrary number of steps as well as :math:`2^{127}` streams.
        The specific member of the PCG family that we use is PCG CM DXSM 128/64. It
        differs from ``PCG64`` in that it uses the stronger DXSM output function,
        a 64-bit "cheap multiplier" in the LCG, and outputs from the state before
        advancing it rather than advance-then-output.
    
        ``PCG64DXSM`` provides a capsule containing function pointers that produce
        doubles, and unsigned 32 and 64- bit integers. These are not
        directly consumable in Python and must be consumed by a ``Generator``
        or similar object that supports low-level access.
    
        Supports the method :meth:`advance` to advance the RNG an arbitrary number of
        steps. The state of the PCG-64 DXSM RNG is represented by 2 128-bit unsigned
        integers.
    
        **State and Seeding**
    
        The ``PCG64DXSM`` state vector consists of 2 unsigned 128-bit values,
        which are represented externally as Python ints. One is the state of the
        PRNG, which is advanced by a linear congruential generator (LCG). The
        second is a fixed odd increment used in the LCG.
    
        The input seed is processed by `SeedSequence` to generate both values. The
        increment is not independently settable.
    
        **Parallel Features**
    
        The preferred way to use a BitGenerator in parallel applications is to use
        the `SeedSequence.spawn` method to obtain entropy values, and to use these
        to generate new BitGenerators:
    
        >>> from numpy.random import Generator, PCG64DXSM, SeedSequence
        >>> sg = SeedSequence(1234)
        >>> rg = [Generator(PCG64DXSM(s)) for s in sg.spawn(10)]
    
        **Compatibility Guarantee**
    
        ``PCG64DXSM`` makes a guarantee that a fixed seed will always produce
        the same random integer stream.
    
        References
        ----------
        .. [1] `"PCG, A Family of Better Random Number Generators"
               <http://www.pcg-random.org/>`_
        .. [2] O'Neill, Melissa E. `"PCG: A Family of Simple Fast Space-Efficient
               Statistically Good Algorithms for Random Number Generation"
               <https://www.cs.hmc.edu/tr/hmc-cs-2014-0905.pdf>`_
    """
    def advance(self, delta): # real signature unknown; restored from __doc__
        """
        advance(delta)
        
                Advance the underlying RNG as-if delta draws have occurred.
        
                Parameters
                ----------
                delta : integer, positive
                    Number of draws to advance the RNG. Must be less than the
                    size state variable in the underlying RNG.
        
                Returns
                -------
                self : PCG64
                    RNG advanced delta steps
        
                Notes
                -----
                Advancing a RNG updates the underlying RNG state as-if a given
                number of calls to the underlying RNG have been made. In general
                there is not a one-to-one relationship between the number output
                random values from a particular distribution and the number of
                draws from the core RNG.  This occurs for two reasons:
        
                * The random values are simulated using a rejection-based method
                  and so, on average, more than one value from the underlying
                  RNG is required to generate an single draw.
                * The number of bits required to generate a simulated value
                  differs from the number of bits generated by the underlying
                  RNG.  For example, two 16-bit integer values can be simulated
                  from a single draw of a 32-bit RNG.
        
                Advancing the RNG state resets any pre-computed random numbers.
                This is required to ensure exact reproducibility.
        """
        pass

    def jumped(self, jumps=1): # real signature unknown; restored from __doc__
        """
        jumped(jumps=1)
        
                Returns a new bit generator with the state jumped.
        
                Jumps the state as-if jumps * 210306068529402873165736369884012333109
                random numbers have been generated.
        
                Parameters
                ----------
                jumps : integer, positive
                    Number of times to jump the state of the bit generator returned
        
                Returns
                -------
                bit_generator : PCG64DXSM
                    New instance of generator jumped iter times
        
                Notes
                -----
                The step size is phi-1 when multiplied by 2**128 where phi is the
                golden ratio.
        """
        pass

    def __init__(self, seed=None): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce_cython__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate_cython__(self, *args, **kwargs): # real signature unknown
        pass

    state = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Get or set the PRNG state

        Returns
        -------
        state : dict
            Dictionary containing the information required to describe the
            state of the PRNG
        """


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x7fd2ef9530c0>'


# variables with complex values

__all__ = [
    'PCG64',
]

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x7fd2ef953010>'

__spec__ = None # (!) real value is "ModuleSpec(name='numpy.random._pcg64', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x7fd2ef953010>, origin='/home/olenepal/.local/lib/python3.10/site-packages/numpy/random/_pcg64.cpython-310-x86_64-linux-gnu.so')"

__test__ = {}

