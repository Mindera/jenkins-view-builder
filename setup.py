#!/usr/bin/env/python

PROJECT = 'jenkins-view-builder'

VERSION = 0.1

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

config = {
    'name': PROJECT,
    'version': VERSION,

    'description': 'Build jenkins views in YAML',

    'author': 'Piyush Srivastava',
    'author_email': 'piyush.0101@gmail.com',

    'url': 'http://jenkins-view-builder.com',
    'download_url': 'Where to download it.',

    'classifiers': ['Development Status :: 3 - Alpha',
                    'License :: Apache Software License',
                    'Programming Language :: Python',
                    'Programming Language :: Python :: 2',
                    'Programming Language :: Python :: 2.7',
                    'Intended Audience :: Developers',
                    'Environment :: Console'],

    'platforms': ['Any'],

    'scripts': [],

    'provides': [],

    'install_requires': ['cliff'],

    'namespace_packages': [],
    'packages': find_packages(),
    'include_package_data': True,

    'entry_points' : {
            'console_scripts' : [
                    'jenkins-view-builder = builder.main:main',
                    ],
            'builder.commands' : [
                        'simple = builder.commands.simple:Simple',
                        'update = builder.commands.update:Update',
                    ],
        },


    'install_requires': ['nose'],
    'packages': find_packages(),
    'scripts': [],

    'zip_safe': False,
}

setup(**config)
