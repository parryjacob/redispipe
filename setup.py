import os
import sys
from setuptools import setup


def read(*paths):
    with open(os.path.join(*paths), 'r') as f:
        return f.read()

setup(
    name='redispipe',
    version='1.0.0',
    description='Wrap a process\' stdin/stdout/stderr pipes with Redis pubsub queues',
    long_description=read('README.md'),
    url='https://github.com/parryjacob/redispipe',
    license='MIT',
    author='Jacob Parry',
    author_email='jacob@jacobparry.ca',
    scripts=['redispipe'],
    include_package_data=False,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Topic :: System :: Systems Administration',
    ],
    install_requires=['redis',]
)
