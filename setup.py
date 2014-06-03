from distutils.core import setup

setup(
    name='comb',
    version='0.8.10',
    packages=['comb', 'comb.mq', 'comb.demo'],
    scripts=['bin/comb'],
    url='https://github.com/kbonez/comb',
    download_url = 'https://github.com/kbonez/comb/tarball/0.8.10',
    license='http://opensource.org/licenses/MIT',
    author='Breeze.Kay',
    author_email='wangwenpei@kbonez.com',
    description='simply and high-performance hook for develop threads program',
    keywords='comb,slot,thread,framework,hook'
)
