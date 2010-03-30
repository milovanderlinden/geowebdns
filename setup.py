from setuptools import setup, find_packages

version = '0.1'

setup(name='geowebdns',
      version=version,
      description="Geographic query web service",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='geo web',
      author='Ian Bicking',
      author_email='ianb@openplans.org',
      url='',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      zip_safe=False,
      install_requires=[
          'WebOb',
          'GeoAlchemy',
          'CmdUtils',
          'httplib2',
          ],
      tests_require=[
          'WebTest',
          ],
      entry_points="""
      [console_scripts]
      geodns-import-shp = geowebdns.importshp:main
      """,
      )
