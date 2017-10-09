#!/usr/bin/env python
"""
ChatterBot Input and Output Adapters setup file.
"""
from setuptools import setup


# Dynamically retrieve the version information from the chatterbot module
CHATTERBOT_ADAPTERS = __import__('chatterbot_io_adapters')
VERSION = CHATTERBOT_ADAPTERS.__version__
AUTHOR = CHATTERBOT_ADAPTERS.__author__
AUTHOR_EMAIL = CHATTERBOT_ADAPTERS.__email__
URL = CHATTERBOT_ADAPTERS.__url__
DESCRIPTION = 'ChatterBots input and output adapters'
LONG_DESCRIPTION = 'ChatterBots input and output adapters'

with open('requirements.txt') as requirements:
    REQUIREMENTS = requirements.readlines()

setup(
    name='chatterbot-io-adapters',
    version=VERSION,
    url=URL,
    download_url='{}/tarball/{}'.format(URL, VERSION),
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    packages=[
        'chatterbot_io_adapters',
        'chatterbot_io_adapters.input',
        'chatterbot_io_adapters.output',
    ],
    package_dir={'chatterbot_io_adapters': 'chatterbot_io_adapters'},
    include_package_data=True,
    install_requires=REQUIREMENTS,
    license='BSD',
    zip_safe=True,
    platforms=['any'],
    keywords=['ChatterBot', 'chatbot', 'chat', 'bot', 'adapters'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Communications :: Chat',
        'Topic :: Internet',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=['mock']
)
