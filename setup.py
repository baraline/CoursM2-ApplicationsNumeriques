
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
	python_requires='>=3.7',
   install_requires=[
        "matplotlib >= 3.5",
        "pandas >= 1.3.4",
        "scikit_learn >= 1.0.2",
        "sktime == 0.9",
        "numpy >= 1.19.3",
    ],
    zip_safe=False
)
