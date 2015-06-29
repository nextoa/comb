from setuptools import setup

import comb

setup(
    name='comb',
    version=comb.version,
    packages=['comb', 'comb.mq', 'comb.demo'],
    install_requires=['cliez'],
    url='http://comb.readthdocs.org',
    license='http://opensource.org/licenses/MIT',
    author='Wang WenPei',
    author_email='wangwenpei@nextoa.com',
    description='A simply and high-performance framework for create concurrent program',
    keywords='comb,slot,thread,framework,hook',
    entry_points={
        'console_scripts': [
            'comb = comb.main:main'
        ]
    },


)
