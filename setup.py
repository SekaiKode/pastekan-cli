#!/usr/bin/env python3

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

try:
    from pypandoc import convert
    read_md = lambda f: convert(f, 'rst')
except ImportError:
    print("warning: pypandoc module not found, could not convert Markdown to RST")
    read_md = lambda f: open(f, 'r').read()

setup(
    name='pastekan',
    version='1.0.1',
    url='https://github.com/SekaiKode/pastekan-cli',
    description='CLI client for pastekan server (pastekan.cf) written in Python.',
    long_description=read_md('README.md'),
    long_description_content_type="text/markdown",
    author='Made Wiguna',
    author_email='madewgn2@gmail.com',
    license='MIT',
    scripts=['pastekan'],
    install_requires=[
        'requests',
        'docopt'
    ],
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Topic :: Utilities'
    ]
)
