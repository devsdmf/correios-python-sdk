
# -*- coding: utf-8 -*-

import unittest
from correios.package import Package

class TestPackage(unittest.TestCase):

    def setUp(self):
        pass

    def test_constructor_default_dimensions(self):
        package = Package()

        self.assertEqual(0.0,package.get_height())
        self.assertEqual(0.0,package.get_width())
        self.assertEqual(0.0,package.get_length())
        self.assertEqual(0.0,package.get_diameter())

    def test_constructor_without_package(self):
        package = Package()

        self.assertEqual(Package.FORMAT_BOX,package.get_format())

    def test_constructor_with_package(self):
        package = Package(Package.FORMAT_CYLINDER)

        self.assertEqual(Package.FORMAT_CYLINDER,package.get_format())
