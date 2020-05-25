import os, sys

from setuptools import setup, find_packages


def read_requirements():
    """Parse requirements from requirements.txt."""

    reqs_path = os.path.join('.', 'requirements.txt')
    with open(reqs_path, 'r') as f:
        requirements = [line.rstrip() for line in f]
    return requirements

setup(
    name='primely',
    version='0.0.1',
    description='Converts paychecks and returns json parameters',
    long_description='README.md',
    author='Yoshiki Nakagawa',
    author_email='ben.nakagawa01@gmail.com',
    install_requires=read_requirements(),
    url='https://github.com/yoshiki-o0/primely_package',
    lincense='LICENCE',
    # packages=find_packages('core_primely'),
    packages=find_packages('src'),
    package_dir={'': 'src'},
    # packages=[
    #     'core_primely.controller',
    #     'core_primely.models',
    #     'core_primely.templates',
    #     'core_primely.views',
    #     'tools'
    # ]
    # ,
    # test_suite='tests'
    package_data={'': ['templates/*.txt']}
)