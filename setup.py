# -*- coding: utf-8 -*-

from setuptools import Command, find_packages, setup
import sys

install_requires = ['requests>=1.0.3']
tests_require = ['pytest', 'httpretty>=0.5.8']


class PyTest(Command):
    description = 'Runs the test suite.'
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        import pytest
        errno = pytest.main('test/unit')
        sys.exit(errno)


setup(name='rdd',
      version='0.2.2',
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
      install_requires=install_requires,
      tests_require=tests_require,
      extras_require={'test': tests_require},
      entry_points="""
      # -*- Entry points: -*-
      [console_scripts]
      rdd=rdd.cli:main
      """,
      cmdclass={'test': PyTest})
