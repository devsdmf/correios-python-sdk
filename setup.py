
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
        tests = test_loader.discover('tests', pattern='text_*.py')
        runner.run(tests)

setup(
    name = 'correios-python-sdk',
    version = '1.0.0',

    description = 'Correios\'s unofficial SDK for Python',
    keywords = 'correios shipping sdk',
    url = 'https://github.com/devsdmf/correios-python-sdk',
    author = 'devsdmf',
    author_email = 'devsdmf@gmail.com',
    license = 'MIT',

    classifiers = [
        'Development Status :: 5 - Production/Stable',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',

        'License :: OSI Approved :: MIT License',

        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],

    packages = find_packages(),
    install_requires = ['requests'],
    cmdclass = {'test': TestRunner}
)
