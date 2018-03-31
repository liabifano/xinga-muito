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
                        'toolz==0.8.0',
                        'requests==2.18.4',
                        'beautifulsoup4==4.6.0',
                        'lxml==4.2.1',
                        'html5lib==1.0.1',
                        'w3lib==1.19.0'],
      include_package_data=True,
      zip_safe=False)