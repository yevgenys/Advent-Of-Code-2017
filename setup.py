from distutils.core import setup
from Cython.Build import cythonize

setup(
    ext_modules=cythonize(["puzzle15.pyx", "puzzle17.pyx"]),
)
