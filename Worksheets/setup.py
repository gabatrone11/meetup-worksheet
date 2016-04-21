from setuptools import setup

# This setup is suitable for "python setup.py develop.

setup(name='mymaths',
      version='0.1',
      description='A simple math package',
      author='Me',
      author_email='me@mymaths.org',
      url='http://www.mymaths.org/',
      packages=['mymaths', 'mymaths.adv'],
      )
      