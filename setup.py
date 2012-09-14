import os
from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='webassets-recess',
    version='0.0.0',
    description='Recess filter to compile less with webassets, enables twitter bootstrap less compiling',
    author='James Pic',
    author_email='jamespic@gmail.com',
    url='http://github.com/yourlabs/webassets-recess',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    long_description=read('README.rst'),
    license='MIT',
    keywords='lesscss recess webassets',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
