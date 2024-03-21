from setuptools import find_packages, setup

setup(
    name='babel-fish',
    packages=find_packages(include=['BabelFish']),
    version='0.0.1',
    description='A framework to drive a clean code',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='v2SoftwareHouse',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
)
