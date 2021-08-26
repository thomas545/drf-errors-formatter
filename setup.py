#!/usr/bin/env python

import os

from setuptools import find_packages, setup

here = os.path.dirname(os.path.abspath(__file__))
f = open(os.path.join(here, 'README.md'))
long_description = f.read().strip()
f.close()


about = {}
with open('drf_handlers/__version__.py', 'r', encoding="utf8") as f:
    exec(f.read(), about)

setup(
    name='drf-errors-formatter',
    version=about['__version__'],
    author='Thomas',
    author_email='imichael@pm.me',
    url='https://github.com/thomas545/drf-errors-formatter',
    description='Format errors in Django Rest Framework',
    license='MIT',
    packages=find_packages(),
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords='django rest errors format-errors api',
    zip_safe=False,
    install_requires=[
        'Django>=2.0',
        'djangorestframework>=3.7.0',
    ],
    tests_require=[
        'coveralls>=1.11.1',
    ],
    test_suite='runtests.runtests',
    include_package_data=True,
    python_requires='>=3.6',
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Topic :: Software Development'
    ],
)
