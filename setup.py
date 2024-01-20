from setuptools import find_packages, setup

classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]

setup(
    name='simple_string_lib',
    packages=find_packages(include=['simple_string_lib']),
    long_description=open('README.md').read() + '\n\n' + open('CHANGELOG.md').read(),
    version='0.1.0',
    description='A simple library for comparing strings.',
    license='MIT',
    classifiers=classifiers,
    keywords='string',
    author='Lenny Siemeni',
    test_suite='tests',
    install_requires=['']
)
