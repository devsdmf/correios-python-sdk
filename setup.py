
from distutils.core import Command
from setuptools import setup, find_packages

class TestRunner(Command):
    """run tests"""

    description = "run unittest to execute all tests"

    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        import unittest
        runner = unittest.runner.TextTestRunner()
        test_loader = unittest.TestLoader()
        test = test_loader.discover('tests')
        runner.run(test)

setup(
    name = 'correios-sdk',
    version = '0.0.1',

    description = 'Correios\'s unofficial SDK for Python',
    keywords = 'correios shipping sdk',
    url = 'https://github.com/devsdmf/correios-python-sdk',
    author = 'devsdmf',
    author_email = 'devsdmf@gmail.com',
    license = 'MIT',

    classifiers = [
        'Development Status :: 2 - Pre-Alpha',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',

        'License :: OSI Approved :: MIT License',

        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3 :: Only'
    ],

    packages = ['correios'],
    install_requires = [],
    cmdclass = {'test': TestRunner}
)
