# makemake - a simple Makefile generator
# (c) 2023 by Andreas Schwenk <contact@compiler-construction.com>
# License: GPLv3

from setuptools import setup

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(name='makemake',
      version='0.2',
      description='A simple makefile generator for C projects',
      long_description=long_description,
      long_description_content_type='text/markdown',
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
