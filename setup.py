# -*- coding: utf-8 -*-

from setuptools import Command, find_packages, setup
import os
import sys
import pytest

install_requires = ['requests>=1.0.3']
tests_require = ['pytest', 'httpretty>=0.5.9']


def test_units():
    """Run all unit tests"""
    return pytest.main('test/unit')

def test_integration():
    """Run all integration tests"""
    return os.system('make prove -C test/integration')


class TestSuite(Command):
    description = 'Runs the entire test suite.'
    user_options = []

    def initialize_options(self): pass

    def finalize_options(self): pass

    def run(self):
        for t in (test_units, test_integration):
            errno = t()
            if errno != 0: break
        sys.exit(errno)


class TestUnits(Command):
    description = 'Runs all unit tests.'
    user_options = [('real-http', None, 'Do not mock HTTP requests')]

    def initialize_options(self):
        self.real_http = None

    def finalize_options(self):
        pass

    def run(self):
        if self.real_http:
            os.environ['REALHTTP'] = '1'
        sys.exit(test_units())


class TestIntegration(Command):
    description = 'Runs all integration tests.'
    user_options = []

    def initialize_options(self): pass

    def finalize_options(self): pass

    def run(self):
        sys.exit(test_integration())


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
      cmdclass={'test': TestSuite,
                'test_units': TestUnits,
                'test_integration': TestIntegration})
