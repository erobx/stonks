''''
Run to install on your system

pip install -e .

Used to test on a vm
'''

from setuptools import find_packages, setup

setup(
    name='stonks',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'flask',
        'pyvis',
    ],
)