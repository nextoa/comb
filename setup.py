from distutils.core import setup

import comb

setup(
    name='comb',
    version=comb.version,
    packages=['comb', 'comb.mq', 'comb.demo'],
    install_requires=['cliez'],
    url='http://comb.readthdocs.org',
    license='http://opensource.org/licenses/MIT',
    download_url='https://github.com/nextoa/comb/archive/master.zip',
    include_package_data=True,
    author='Wang WenPei',
    author_email='wangwenpei@nextoa.com',
    description='A simple and high-performance framework for create concurrent program',
    keywords='comb,thread,framework,hook',
    entry_points={
        'console_scripts': [
            'comb = comb.main:main'
        ]
    },

)
