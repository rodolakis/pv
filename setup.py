from setuptools import setup, find_packages
from setuptools.command.install import install
import os


setup(
    name='pv',
    version=open('VERSION').read().strip(),
    #version=__version__,
    author='Francesco De Carlo, Tao Zhou, Fanny Rodolakis, Byeongdu Lee',
    author_email='decarlof@gmail.com',
    url='https://github.com/xray-imaging/pv',
    packages=find_packages(),
    include_package_data = True,
    scripts=['bin/pv'],
    description='cli to log and publish EPICS PV on slack',
    zip_safe=False,
)