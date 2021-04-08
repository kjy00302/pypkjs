__author__ = 'katharine'

from setuptools import setup, find_packages

requirements = [
    'gevent>=1.5.0',
    'gevent-websocket>=0.9.3',
    'greenlet>=0.4.7',
    'peewee>=3.0.0',
    'pygeoip>=0.3.2',
    'pypng>=0.0.17',
    'python-dateutil>=2.4.1',
    'requests>=2.7.0',
    'sh>=1.09',
    'six>=1.9.0',
    'websocket-client>=0.32.0',
    'libpebble2>=0.0.20',
    'netaddr>=0.7.18',
    'stpyv8 >= 8'
]

__version__= None  # Overwritten by executing version.py.
with open('pypkjs/version.py') as f:
    exec(f.read())

setup(name='pypkjs',
      version=__version__,
      description='A Pebble phone app simulator written in Python',
      url='https://github.com/pebble/pypkjs',
      author='Pebble Technology Corporation',
      author_email='katharine@pebble.com',
      license='MIT',
      packages=find_packages(),
      install_requires=requirements,
      package_data={
          'pypkjs.javascript.navigator': ['GeoLiteCity.dat'],
          'pypkjs.timeline': ['layouts.json'],
      },
      entry_points={
          'console_scripts': [
            'pypkjs=pypkjs.runner.websocket:run_tool'
          ],
      },
      zip_safe=False)
