# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import rdd

setup(name='rdd',
      version=rdd.__version__,
      author='Mathias Lafeldt',
      author_email='mathias.lafeldt@gmail.com',
      url='https://github.com/mlafeldt/rdd.py',
      license='MIT',
      description='Python implementation of the Readability Shortener API',
      long_description=open('README.md').read() + '\n\n' +
                       open('HISTORY.rst').read(),
      classifiers=['Development Status :: 4 - Beta',
                   'Intended Audience :: Developers',
                   'Natural Language :: English',
                   'License :: OSI Approved :: MIT License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python'],
      packages=find_packages(),
      zip_safe=False,
      setup_requires=[],
      install_requires=['requests>=0.12.1'],
      entry_points="""
      # -*- Entry points: -*-
      [console_scripts]
      rdd=rdd.cli:main
      """)
