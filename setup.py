from setuptools import setup

setup(
    name='beets-missingalbums',
    version='0.0.1',
    description='beets plugin to list albums by artists you like not in your collection',
    long_description=open('README.md').read(),
    author='Jonathan Harrington',
    author_email='jonathan@jonharrington.org',
    url='http://www.github.com/prio/missingalbums',
    license='BSD',
    platforms='ALL',

    packages=['beetsplug'],

    install_requires=[
        'beets>=1.3.4',
    ],

    classifiers=[
        'Topic :: Multimedia :: Sound/Audio',
        'Topic :: Multimedia :: Sound/Audio :: Players :: MP3',
        'License :: OSI Approved :: MIT License',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],
)
