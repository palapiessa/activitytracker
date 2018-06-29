#!/usr/bin/env python

PROJECT = 'activitytracker'

# Change docs/sphinx/conf.py too!
VERSION = '0.1'

from setuptools import setup, find_packages

try:
    long_description = open('README.rst', 'rt').read()
except IOError:
    long_description = ''

setup(
    name=PROJECT,
    version=VERSION,

    description='Activity & time tracker app',
    long_description=long_description,

    author='Petri Alapiessa',
    author_email='palapiessa@gmail.com',

    url='https://github.com/palapiessa/activitytracker',

    classifiers=['Development Status :: 3 - Alpha',
                 'License :: OSI Approved :: Apache Software License',
                 'Programming Language :: Python',
                 'Programming Language :: Python :: 2',
                 'Programming Language :: Python :: 2.7',
                 'Programming Language :: Python :: 3',
                 'Programming Language :: Python :: 3.2',
                 'Intended Audience :: Developers',
                 'Environment :: Console',
                 ],

    platforms=['Any'],

    scripts=[],

    provides=[],
    install_requires=['cliff'],

    namespace_packages=[],
    packages=find_packages(),
    include_package_data=True,

    entry_points={
        'console_scripts': [
            'activitytracker = activitytracker.main:main'
        ],
        'activity.tracker': [
            'start = activitytracker.start:Start',
            'stop = activitytracker.stop:Stop',
        ],
    },

    zip_safe=False,
)
