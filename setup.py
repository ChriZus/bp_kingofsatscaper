from setuptools import setup, find_packages

version = '0.2.0'

REQUIREMENTS = [
    'scrapy'
]

setup(
    name='bp_kingofsat',
    version=version,
    packages=find_packages(),
    author='Chris van den Berg',
    author_email='chrizus@gmail.com',
    install_requires=REQUIREMENTS,
    description='Scrapy library which uses channel parsing from kingofsat. original author: Enes Emre BULUT (bulutenesemre@gmail.com)',
    include_package_data=True
)
