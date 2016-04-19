# -*- coding: utf-8 -*-
#
#  setup.py
#  cjktools
#

"""
Package setup file for the cjktools package.
"""

import sys
from setuptools import setup

VERSION = '1.7.0'

f = open('cjktools/__version__.py', 'w')
f.write('# Autogenerated by setup.py\n')
f.write('version = "%s"\n' % VERSION)
f.close()

LONG_DESCRIPTION = \
"""
Provides basic script detection, manipulation of kana and interfaces
for the popular EDICT and KANJIDIC families of dictionaries.
"""

# For Python <= 3.4, we need to pull in the backport of enum
REQUIRES = ['six']
if sys.version_info < (3, 4, 0):
    REQUIRES.append('enum34')

# Set up the classifiers
CLASSIFIERS = [
'License :: OSI Approved :: BSD License',
'Programming Language :: Python',
'Programming Language :: Python :: 2',
'Programming Language :: Python :: 2.7',
'Programming Language :: Python :: 3',
'Programming Language :: Python :: 3.4',
'Programming Language :: Python :: 3.5',
]

setup(
    name='cjktools',
    description="A library for basic CJK processing and lexicography.",
    version=VERSION,
    long_description=LONG_DESCRIPTION,
    classifiers=CLASSIFIERS,
    url="https://github.com/larsyencken/cjktools",
    author="Lars Yencken",
    author_email="lars@yencken.org",
    license="BSD",
    install_requires=REQUIRES,
    package_dir={'cjktools': 'cjktools'},
    packages=['cjktools', 'cjktools.resources'],
    test_suite='cjktools.tests'
)
