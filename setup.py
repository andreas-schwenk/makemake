# makemake - a simple Makefile generator
# (c) 2023 by Andreas Schwenk <contact@compiler-construction.com>
# License: GPLv3

from setuptools import setup

setup(name='makemake',
      version='0.1',
      description='A simple makefile generator for C projects',
      long_description='Creates a makefile from a source folder and a Makefile.in file',
      classifiers=[
          'Development Status :: 4 - Beta',
          'Intended Audience :: Developers',
          'Topic :: Software Development :: Build Tools',
          'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
          'Programming Language :: Python :: 3.9',
      ],
      keywords='make makefile C build',
      url='https://github.com/andreas-schwenk/makemake',
      author='Andreas Schwenk',
      author_email='contact@compiler-construction.com',
      license='GPLv3',
      packages=['makemake'],
      scripts=['bin/makemake'],
      include_package_data=True,
      zip_safe=False)
