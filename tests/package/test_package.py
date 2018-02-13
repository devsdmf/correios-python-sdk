# -*- coding: utf-8 -*-

import unittest
from correios.package import Package, BoxPackage, CylinderPackage, EnvelopePackage

class TestPackage(unittest.TestCase):

    def setUp(self):
        pass
    
    def test_create_package(self):
        package = Package()
        self.assertEqual(Package.FORMAT_BOX,package.get_format())
    
    def test_create_package_with_different_format(self):
        package = Package(Package.FORMAT_CYLINDER)
        self.assertEqual(Package.FORMAT_CYLINDER,package.get_format())
    
    def test_package_is_format(self):
        package = Package(Package.FORMAT_CYLINDER)
        self.assertTrue(package.is_format(Package.FORMAT_CYLINDER))
    
    def test_abstract_add_item_raises_exception(self):
        package = Package()
        with self.assertRaises(NotImplementedError):
            package.add_item()
    
    def test_check_for_items_in_emtpy_package(self):
        package = Package()
        self.assertFalse(package.has_items())
    
    def test_check_for_items_in_non_empty_package(self):
        package = Package()
        package.items = [1]
        self.assertTrue(package.has_items())

    def test_get_items_from_empty_package(self):
        package = Package()
        items = package.get_items()
        self.assertEqual(0,len(items))
    
    def test_get_items_from_non_empty_package(self):
        package = Package()
        package.items = [1]
        items = package.get_items()
        self.assertGreater(len(items),0)
    
    def test_abstract_get_dimensions_raises_exception(self):
        package = Package()
        with self.assertRaises(NotImplementedError):
            package.get_dimensions()
    
    def test_get_weight_from_empty_package(self):
        package = Package()
        self.assertEqual(0,package.get_weight())
    
    def test_abstract_is_valid_raises_exception(self):
        package = Package()
        with self.assertRaises(NotImplementedError):
            package.is_valid()
    
    def test_abstract_api_format_raises_exception(self):
        package = Package()
        with self.assertRaises(NotImplementedError):
            package.api_format()

class TestBoxPackage(unittest.TestCase):

    def setUp(self):
        pass
    
    def test_create_box_package(self):
        package = BoxPackage()
        self.assertEqual(Package.FORMAT_BOX,package.get_format())
    
    def test_add_single_item_to_box_package(self):
        height = 1.0
        width = 2.0
        depth = 3.0
        weight = 0.3

        package = BoxPackage()
        package.add_item(height,width,depth,weight)
        
        self.assertTrue(package.has_items())
        self.assertEqual(height,package.get_items()[0].height)
        self.assertEqual(width,package.get_items()[0].width)
        self.assertEqual(depth,package.get_items()[0].depth)
        self.assertEqual(weight,package.get_items()[0].weight)
    
    def test_add_multiple_items_to_box_package(self):
        height0 = 1.0
        width0 = 2.0
        depth0 = 3.0
        weight0 = 0.3

        height1 = 2.0
        width1 = 3.0
        depth1 = 4.0
        weight1 = 1.0

        package = BoxPackage()
        package.add_item(height0,width0,depth0,weight0)
        package.add_item(height1,width1,depth1,weight1)

        self.assertTrue(package.has_items())

        self.assertEqual(height0,package.get_items()[0].height)
        self.assertEqual(width0,package.get_items()[0].width)
        self.assertEqual(depth0,package.get_items()[0].depth)
        self.assertEqual(weight0,package.get_items()[0].weight)

        self.assertEqual(height1,package.get_items()[1].height)
        self.assertEqual(width1,package.get_items()[1].width)
        self.assertEqual(depth1,package.get_items()[1].depth)
        self.assertEqual(weight1,package.get_items()[1].weight)
    
    def test_get_dimensions_for_single_item_box_package_with_minimum_dimensions(self):
        height = 1.0
        width = 2.0
        depth = 3.0

        package = BoxPackage()
        package.add_item(height,width,depth,0.3)

        dimensions = package.get_dimensions()
        self.assertTupleEqual(dimensions,(BoxPackage.MIN_HEIGHT,BoxPackage.MIN_WIDTH,BoxPackage.MIN_DEPTH))
    
    def test_get_dimensions_for_single_item_box_package_with_dimensions_over_the_minimum(self):
        height = 15.0
        width = 20.0
        depth = 25.0

        package = BoxPackage()
        package.add_item(height,width,depth,0.3)

        dimensions = package.get_dimensions()
        self.assertTupleEqual(dimensions,(height,width,depth))
    
    def test_get_dimensions_for_multiple_items_box_package_with_minimum_dimensions(self):
        height0 = 0.5
        width0 = 0.5
        depth0 = 0.5
        weight0 = 0.3

        height1 = 0.5
        width1 = 0.8
        depth1 = 0.6
        weight1 = 1.0

        package = BoxPackage()
        package.add_item(height0,width0,depth0,weight0)
        package.add_item(height1,width1,depth1,weight1)

        dimensions = package.get_dimensions()
        self.assertTupleEqual(dimensions,(BoxPackage.MIN_HEIGHT,BoxPackage.MIN_WIDTH,BoxPackage.MIN_DEPTH))
    
    def test_get_dimensions_for_multiple_items_box_package_with_dimensions_over_the_minimum(self):
        height0 = 10
        width0 = 12
        depth0 = 25
        weight0 = 0.3

        height1 = 6
        width1 = 14
        depth1 = 20
        weight1 = 1.0

        package = BoxPackage()
        package.add_item(height0,width0,depth0,weight0)
        package.add_item(height1,width1,depth1,weight1)

        dimensions = package.get_dimensions()
        self.assertTupleEqual(dimensions,(height0 + height1,width1,depth0))
    
    def test_get_weight_of_box_package(self):
        weight0 = 0.5
        weight1 = 1.5

        package = BoxPackage()
        package.add_item(1.0,2.0,3.0,weight0)
        package.add_item(2.0,3.0,5.0,weight1)

        self.assertEqual(weight0 + weight1,package.get_weight())
    
    def test_check_for_valid_box_package_with_valid_dimensions(self):
        package = BoxPackage()
        package.add_item(15.0,20.0,35.0,1.2)
        self.assertTrue(package.is_valid())
    
    def test_check_for_valid_box_package_with_exceeded_dimensions(self):
        package = BoxPackage()
        package.add_item(BoxPackage.MAX_HEIGHT+1.0,BoxPackage.MAX_WIDTH+1.0,BoxPackage.MAX_DEPTH+1.0,2.0)
        self.assertFalse(package.is_valid())
    
    def test_check_for_valid_box_package_with_exceeded_volume(self):
        package = BoxPackage()
        package.add_item(100.0,100.0,100.0,5.0)
        self.assertFalse(package.is_valid())
    
    def test_api_format_for_valid_box_package(self):
        height = 15.0
        width = 20.0
        depth = 35.0
        weight = 1.2

        package = BoxPackage()
        package.add_item(height,width,depth,weight)
        expected = {
            'nCdFormato': Package.FORMAT_BOX,
            'nVlAltura': height,
            'nVlLargura': width,
            'nVlComprimento': depth,
            'nVlPeso': weight
        }
        self.assertDictEqual(package.api_format(),expected)
    
    def test_api_format_for_invalid_box_package(self):
        package = BoxPackage()
        package.add_item(100.0,100.0,100.0,5.0)
        with self.assertRaises(Exception):
            package.api_format()

class TestCylinderPackage(unittest.TestCase):

    def setUp(self):
        pass
    
    def test_create_cylinder_package(self):
        package = CylinderPackage()
        self.assertEqual(Package.FORMAT_CYLINDER,package.get_format())
    
    def test_add_single_item_to_cylinder_package(self):
        length = 5.0
        diameter = 1.0
        weight = 0.5

        package = CylinderPackage()
        package.add_item(length,diameter,weight)

        self.assertTrue(package.has_items())
        self.assertEqual(length,package.get_items()[0].length)
        self.assertEqual(diameter,package.get_items()[0].diameter)
        self.assertEqual(weight,package.get_items()[0].weight)
    
    def test_add_multiple_items_to_cylinder_package(self):
        length0 = 5.0
        diameter0 = 1.0
        weight0 = 0.3

        length1 = 10.0
        diameter1 = 2.0
        weight1 = 0.5

        package = CylinderPackage()
        package.add_item(length0,diameter0,weight0)
        package.add_item(length1,diameter1,weight1)

        self.assertTrue(package.has_items())

        self.assertEqual(length0,package.get_items()[0].length)
        self.assertEqual(diameter0,package.get_items()[0].diameter)
        self.assertEqual(weight0,package.get_items()[0].weight)

        self.assertEqual(length1,package.get_items()[1].length)
        self.assertEqual(diameter1,package.get_items()[1].diameter)
        self.assertEqual(weight1,package.get_items()[1].weight)
    
    def test_get_dimensions_for_single_item_cylinder_package_with_minimum_dimensions(self):
        length = 5.0
        diameter = 1.0

        package = CylinderPackage()
        package.add_item(length,diameter,0.5)

        dimensions = package.get_dimensions()
        self.assertTupleEqual(dimensions,(CylinderPackage.MIN_LENGTH,CylinderPackage.MIN_DIAMETER))
    
    def test_get_dimensions_for_single_item_cylinder_package_with_dimensions_over_the_minimum(self):
        length = 60.0
        diameter = 10.0

        package = CylinderPackage()
        package.add_item(length,diameter,2.0)

        dimensions = package.get_dimensions()
        self.assertTupleEqual(dimensions,(length,diameter))
    
    def test_get_dimensions_for_multiple_items_cylinder_package_with_minimum_dimensions(self):
        length0 = 5.0
        diameter0 = 1.0

        length1 = 10.0
        diameter1 = 2.0

        package = CylinderPackage()
        package.add_item(length0,diameter0,0.5)
        package.add_item(length1,diameter1,0.8)

        dimensions = package.get_dimensions()
        self.assertTupleEqual(dimensions,(CylinderPackage.MIN_LENGTH,CylinderPackage.MIN_DIAMETER))
    
    def test_get_dimensions_for_multiple_items_cylinder_package_with_dimensions_over_the_minimum(self):
        length0 = 25.0
        diameter0 = 5.0

        length1 = 30.0
        diameter1 = 12.0

        package = CylinderPackage()
        package.add_item(length0,diameter0,0.5)
        package.add_item(length1,diameter1,0.8)

        dimensions = package.get_dimensions()
        self.assertTupleEqual(dimensions,(length0 + length1,diameter1))
    
    def test_get_weight_of_cylinder_package(self):
        weight0 = 5.0
        weight1 = 12.5

        package = CylinderPackage()
        package.add_item(1.0,2.0,weight0)
        package.add_item(2.0,3.0,weight1)

        self.assertEqual(package.get_weight(),weight0 + weight1)
    
    def test_check_for_valid_cylinder_package_with_valid_dimensions(self):
        package = CylinderPackage()
        package.add_item(40.0,10.0,0.5)
        self.assertTrue(package.is_valid())
    
    def test_check_for_valid_cylinder_package_with_exceeded_dimensions(self):
        package = CylinderPackage()
        package.add_item(150.0,2.0,0.5)
        self.assertFalse(package.is_valid())
    
    def test_check_for_valid_cylinder_package_with_exceeded_volume(self):
        package = CylinderPackage()
        package.add_item(102.0,50.0,1.0)
        self.assertFalse(package.is_valid())
    
    def test_api_format_for_valid_cylinder_package(self):
        length = 40.0
        diameter = 10.0
        weight = 1.0

        package = CylinderPackage()
        package.add_item(length,diameter,weight)
        expected = {
            'nCdFormato': Package.FORMAT_CYLINDER,
            'nVlComprimento': length,
            'nVlDiametro': diameter,
            'nVlPeso': weight
        }
        self.assertDictEqual(package.api_format(),expected)
    
    def test_api_format_for_invalid_cylinder_package(self):
        package = CylinderPackage()
        package.add_item(102.5,50.0,5.0)
        with self.assertRaises(Exception):
            package.api_format()

class TestEnvelopePackage(unittest.TestCase):

    def setUp(self):
        pass
    
    def test_create_envelope_package(self):
        package = EnvelopePackage()
        self.assertEqual(Package.FORMAT_ENVELOPE,package.get_format())
    
    def test_add_single_item_to_envelope_package(self):
        width = 11.0
        length = 20.0
        weight = 0.3

        package = EnvelopePackage()
        package.add_item(width,length,weight)

        self.assertTrue(package.has_items())
        self.assertEqual(width,package.get_items()[0].width)
        self.assertEqual(length,package.get_items()[0].length)
        self.assertEqual(weight,package.get_items()[0].weight)
    
    def test_add_multiple_items_to_envelope_package(self):
        width0 = 11.0
        length0 = 20.0
        weight0 = 0.3

        width1 = 15.0
        length1 = 25.0
        weight1 = 0.5

        package = EnvelopePackage()
        package.add_item(width0,length0,weight0)
        package.add_item(width1,length1,weight1)

        self.assertTrue(package.has_items())

        self.assertEqual(width0,package.get_items()[0].width)
        self.assertEqual(length0,package.get_items()[0].length)
        self.assertEqual(weight0,package.get_items()[0].weight)

        self.assertEqual(width1,package.get_items()[1].width)
        self.assertEqual(length1,package.get_items()[1].length)
        self.assertEqual(weight1,package.get_items()[1].weight)
    
    def test_get_dimensions_for_single_item_envelope_package_with_minimum_dimensions(self):
        width = 5.0
        length = 10.0

        package = EnvelopePackage()
        package.add_item(width,length,0.3)

        dimensions = package.get_dimensions()
        self.assertTupleEqual(dimensions,(EnvelopePackage.MIN_WIDTH,EnvelopePackage.MIN_LENGTH))
    
    def test_get_dimensions_for_single_item_envelope_package_with_dimensions_over_the_minimum(self):
        width = 25.0
        length = 40.0

        package = EnvelopePackage()
        package.add_item(width,length,0.5)

        dimensions = package.get_dimensions()
        self.assertTupleEqual(dimensions,(width,length))
    
    def test_get_dimensions_for_multiple_items_envelope_package_with_minimum_dimensions(self):
        width0 = 5.0
        length0 = 5.0

        width1 = 10.0
        length1 = 10.0

        package = EnvelopePackage()
        package.add_item(width0,length0,0.5)
        package.add_item(width1,length1,0.8)

        dimensions = package.get_dimensions()
        self.assertTupleEqual(dimensions,(EnvelopePackage.MIN_WIDTH,EnvelopePackage.MIN_LENGTH))
    
    def test_get_dimensions_for_multiple_items_envelope_package_with_dimensions_over_the_minimum(self):
        width0 = 20.0
        length0 = 10.0

        width1 = 10.0
        length1 = 25.0

        package = EnvelopePackage()
        package.add_item(width0,length0,0.5)
        package.add_item(width1,length1,0.8)

        dimensions = package.get_dimensions()
        self.assertTupleEqual(dimensions,(width0,length1))
    
    def test_get_weight_of_envelope_package(self):
        weight0 = 4.0
        weight1 = 9.0

        package = EnvelopePackage()
        package.add_item(5.0,5.0,weight0)
        package.add_item(15.0,10.0,weight1)

        self.assertEqual(package.get_weight(),weight0 + weight1)
    
    def test_check_for_valid_envelope_package_with_valid_dimensions(self):
        package = EnvelopePackage()
        package.add_item(13.0,25.0,0.5)
        self.assertTrue(package.is_valid())
    
    def test_check_for_valid_envelope_package_with_exceeded_dimensions(self):
        package = EnvelopePackage()
        package.add_item(65.0,70.0,0.5)
        self.assertFalse(package.is_valid())
    
    def test_check_for_valid_envelope_package_with_exceeded_weight(self):
        package = EnvelopePackage()
        package.add_item(13.0,25.0,1.2)
        self.assertFalse(package.is_valid())
    
    def test_api_format_for_valid_envelope_package(self):
        width = 13.0
        length = 25.0
        weight = 0.5

        package = EnvelopePackage()
        package.add_item(width,length,weight)
        expected = {
            'nCdFormato': Package.FORMAT_ENVELOPE,
            'nVlAltura': 0.0,
            'nVlLargura': width,
            'nVlComprimento': length,
            'nVlPeso': weight
        }
        self.assertDictEqual(package.api_format(),expected)
    
    def test_api_format_for_invalid_envelope_package(self):
        package = EnvelopePackage()
        package.add_item(65.0,70.0,0.5)
        with self.assertRaises(Exception):
            package.api_format()
