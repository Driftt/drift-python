from setuptools import setup
from drift import __version__

setup(name='drift-python',
      version=__version__,
      description="A Simple Drift API Wrapper.",
      long_description=open('README.md').read(),
      author='Drift Engineering',
      author_email='driftintegrations@drift.com',
      packages=['drift'],
      url='https://github.com/Driftt/drift-python',
      include_package_data=True,
      zip_safe=False,
      license='MIT',
      install_requires=[
          'requests==2.19.1',
      ])
