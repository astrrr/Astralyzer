from setuptools import setup, find_packages

setup(
    name='astralyzer',
    version='0.2',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'numpy',
        'matplotlib',
        'seaborn'
    ],
    author='Astr',
    author_email='invisibile.sek@gmail.com',
    description='Astralyzer: Analyzer tool for visualizing and analyzing data',
    url='https://github.com/astrrr/Astralyzer',
)
