from setuptools import setup, find_packages
import sys, os

version = '0.1'

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()


tests_require = [
    'WebTest',
    'mock',
    'pytest',
    'pytest-cov',
    'pytest-xdist',
    'wsgi_intercept',
    'zope.testbrowser',
    ]

setup(name='kotti_etherpad',
      version=version,
      description="Etherpad integration for Kotti",
      long_description=README,
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
          'Kotti>=0.6.0b1',
      ],
      tests_require=tests_require,
      extras_require={
          'testing': tests_require,
          },
      entry_points="""
      # -*- Entry points: -*-
      """,
      message_extractors={'kotti_etherpad': [
            ('**.py', 'lingua_python', None),
            ('**.zcml', 'lingua_xml', None),
            ('**.pt', 'lingua_xml', None),
            ]},
      )
