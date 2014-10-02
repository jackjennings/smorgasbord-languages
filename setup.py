from setuptools import setup

setup(
    name='smorgasbord-languages',
    version='1.0.0',
    author='Jack Jennings',
    author_email='j@ckjennin.gs',
    packages=['smorgasbord-languages'],
    url='http://github.com/jackjennings/smorgasbord-languages',
    license='MIT',
    description='Reports language coverage given a set of unicode values',
    long_description=open('README.rst').read(),
    install_requires=['unicodeset'],
    include_package_data=True
)
