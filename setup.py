from setuptools import setup, find_packages
import os, sys

execfile('MockS3/__version__.py')

setup(name="MockS3",
      description=open(os.path.join(os.path.dirname(__file__), 'README.rst')).read(),
      version=__version__,
      url="http://github.com/unpluggd/MockS3",
      packages=find_packages(exclude="specs"),
      install_requires=['boto',],
      )
