import io
import os
from setuptools import setup

version_txt = os.path.join(os.path.dirname(__file__), 'fenwick', 'version.txt')
with open(version_txt, 'r') as f:
    version = f.read().strip()

with io.open('README.rst', encoding='utf8') as f:
    long_description = f.read()

setup(
    name='fenwick',
    packages=['fenwick'],
    package_data={'fenwick': ['version.txt']},
    license='MIT',
    version=version,
    description='A Python implementation of Fenwick trees',
    long_description=long_description,
    author='Daniel Steinberg',
    author_email='ds@dannyadam.com',
    url='https://github.com/dstein64/fenwick',
    keywords=['fenwick', 'binary-index-tree', 'fenwick-tree'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Unix',
        'Operating System :: POSIX :: Linux',
        'Operating System :: MacOS',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ]
)
