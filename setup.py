try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

__version__ = "0.1.0"

setup(
    name="py-licor",
    version=__version__,
    packages=["licor"],
    description="",
    author="David H Hagan",
    author_email="david.hagan@quant-aq.com",
    license="MIT",
    url="https://github.com/quant-aq/py-licor",
    keywords=["co2"],
    install_requires=["bs4", "pyserial"],
    
)