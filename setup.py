from setuptools import setup, find_packages


with open('README.md') as f:
    README = f.read()

with open('LICENSE') as f:
    LICENSE = f.read()

setup(
    name='ghlint',
    version='0.1.0',
    description='foo',
    long_description=README,
    author='Martin Buberl',
    author_email='hello@martinbuberl.com',
    url='https://github.com/martinbuberl/ghlint',
    license=LICENSE,
    packages=find_packages(exclude=('tests', 'docs'))
)
