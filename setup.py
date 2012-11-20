from setuptools import setup, find_packages
import os

version = '0.4'

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

long_description = (
    read('README.rst')
    + '\n' +
    read('THANKS.txt')
    + '\n' +
    read('CHANGES.txt'))

setup(name='kotti_etherpad',
      version=version,
      description="Etherpad integration into your Kotti site",
      long_description=long_description,
      classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Framework :: Pylons',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
        'License :: Repoze Public License',
      ],
      keywords='kotti etherpad',
      author='Marco Scheihuber',
      author_email='j23d@jusid.de',
      url='http://pypi.python.org/pypi/kotti_etherpad/',
      license='BSD-derived (http://www.repoze.org/LICENSE.txt)',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'Kotti',
      ],
      extras_require={},
      entry_points="""
      [fanstatic.libraries]
      kotti_etherpad = kotti_etherpad.fanstatic:library
      """,
      message_extractors={'kotti_etherpad': [
            ('**.py', 'lingua_python', None),
            ('**.zcml', 'lingua_xml', None),
            ('**.pt', 'lingua_xml', None),
            ]},
      )
