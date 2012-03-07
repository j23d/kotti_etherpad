from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='kotti_etherpad',
      version=version,
      description="Etherpad integration for Kotti",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='kotti etherpad',
      author='j23d',
      author_email='j23d@jusid.de',
      url='jusid.de',
      license='GPL',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'Kotti>=0.5.1',
          #'PyEtherpadLite',
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
