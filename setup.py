from setuptools import setup

setup(name='binary_diffraction',
      version='0.1',
      description='Calculate binary diffraction',
      url='',
      author='ftimmer',
      author_email='ftimmer@uos.de',
      license='MIT',
      packages=['binary_diffraction'],
      zip_safe=False,
      entry_points={
              'console_scripts': ['test=binary_diffraction.main:main'],
              })