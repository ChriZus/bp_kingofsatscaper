from setuptools import setup, find_packages

version = '0.1.0'

REQUIREMENTS = [
    'scrapy'
]

setup(
    name='kingofsat',
    version=version,
    packages=find_packages(),
    author='Enes Emre BULUT',
    author_email='bulutenesemre@gmail.com',
    install_requires=REQUIREMENTS,
    description='Scrapy library which uses channel parsing from kingofsat',
    include_package_data=True
)
