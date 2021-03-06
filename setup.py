#!/usr/bin/python

from distutils.core import setup

# Remember to change in reroute/__init__.py as well!
VERSION = '1.1.1'

setup(
    name='django-reroute',
    version=VERSION,
    description="A drop-in replacement for django.conf.urls.defaults which supports HTTP verb dispatch and view wrapping.",
    long_description=open('README.rst').read(),
    author='Mark Sandstrom',
    author_email='mark@deliciouslynerdy.com',
    url='http://github.com/dnerdy/django-reroute',
    keywords=['reroute', 'django', 'http', 'rest', 'route', 'routing', 'dispatch', 'wrapper'],
    packages=['reroute'],
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Framework :: Django',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
