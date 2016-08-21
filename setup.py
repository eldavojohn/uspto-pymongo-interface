from setuptools import setup, find_packages

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='USPTO Pymongo Example Project',
    version='0.0.1',
    description='This is a sample project for a friend.',
    long_description=readme,
    author='eldavojohn',
    author_email='eldavojohn@gamil.com',
    url='https://github.com/eldavojohn/uspto-pymongo-interface',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
