
import m2tpdm

from setuptools import setup, find_packages
from codecs import open
import numpy
import os

ROOT = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(ROOT, 'README.md'), encoding="utf-8") as f:
    README = f.read()
	
setup(
    name="m2tpdm",
    description="Package containing exercice for students",
	long_description_content_type='text/markdown',
	long_description=README,
    author="Antoine Guillaume",
    packages=find_packages(),
	license='BSD 2',
   version=m2tpdm.__version__,
	url="https://github.com/baraline/CoursM2-ApplicationsNumeriques",
   author_email="antoine.guillaume45@gmail.com",
	python_requires='>=3.6.9',
   install_requires=[
        "pandas >= 1.1",
        "scikit_learn >= 0.24.0",
        "sktime == 0.9",
        "numpy >= 1.19.3",
    ],
    zip_safe=True
)
