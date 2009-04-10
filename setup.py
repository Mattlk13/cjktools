# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------#
# setup.py
# Lars Yencken <lars.yencken@gmail.com>
# vim: ts=4 sw=4 sts=4 et tw=78:
# Wed Jun 27 12:30:37 2007
#
#----------------------------------------------------------------------------#

"""
Package setup file for the cjktools package.
"""

#----------------------------------------------------------------------------#

from setuptools import setup
import os
import re

#----------------------------------------------------------------------------#

VERSION = '1.3.0'

f = open('src/__version__.py', 'w')
f.write('# Autogenerated by setup.py\n')
f.write('version = "%s"\n' % VERSION)
f.close()

setup(
        name='cjktools',
        description="A library for basic CJK processing and lexicography.",
        long_description = """
        Provides basic script detection, manipulation of kana and interfaces
        for the popular EDICT and KANJIDIC families of dictionaries.
        """,
        url="http://bitbucket.org/lars512/cjktools/",
        version=VERSION,
        author="Lars Yencken",
        author_email="lljy@csse.unimelb.edu.au",
        license="BSD",

        package_dir={'cjktools': 'src'},
        packages=['cjktools', 'cjktools.resources'],
        scripts=['src/dyntest.py'],
    )
