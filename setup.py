#!/usr/bin/env python
from setuptools import setup, find_packages


setup(name='xinga-muito',
      url='',
      author='Luis Carlos Marinho',
      package_dir={'': 'src'},
      packages=find_packages('src'),
      version='0.0.1',
      install_requires=['pytest==2.9.2',
                        'mock==2.0.0',
                        'boto==2.38.0',
                        'oauth2==1.9.0.post1',
                        'peewee==2.8.0',
                        'pandas==0.22.0',
                        'toolz==0.8.0'],
      include_package_data=True,
      zip_safe=False)