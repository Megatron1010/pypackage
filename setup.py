from setuptools import setup, find_packages


setup(
    name='pypackage',
    version='0.2',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA Sort & recursion python package',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/Megatron1010/pypackage',
    author='Anga Tinzi',
    author_email='atinzi@gmail.com'
    )
