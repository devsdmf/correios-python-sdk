# -*- coding: utf-8 -*-

import unittest
from correios.package import Item, BoxItem, CylinderItem, EnvelopeItem

class TestItem(unittest.TestCase):

    def setUp(self):
        pass

    def test_create_item(self):
        item = Item(1.0)
        self.assertEqual(1.0,item.weight)
    
    def test_create_item_with_invalid_weight(self):
        with self.assertRaises(Exception):
            item = Item(0.0)

class TestBoxItem(unittest.TestCase):

    def setUp(self):
        pass
    
    def test_create_box_item(self):
        height = 1.0
        width = 2.0
        depth = 3.0
        weight = 0.3

        item = BoxItem(height,width,depth,weight)
        self.assertEqual(height,item.height)
        self.assertEqual(width,item.width)
        self.assertEqual(depth,item.depth)
        self.assertEqual(weight,item.weight)
    
    def test_create_box_item_with_invalid_height(self):
        with self.assertRaises(Exception):
            item = BoxItem(0.0,1.0,1.0,0.3)
    
    def test_create_box_item_with_invalid_width(self):
        with self.assertRaises(Exception):
            item = BoxItem(1.0,0.0,1.0,0.3)
    
    def test_create_box_item_with_invalid_depth(self):
        with self.assertRaises(Exception):
            item = BoxItem(1.0,1.0,0.0,0.3)

class TestCylinderItem(unittest.TestCase):

    def setUp(self):
        pass
    
    def test_create_cylinder_item(self):
        length = 5.0
        diameter = 1.0
        weight = 0.3

        item = CylinderItem(length,diameter,weight)
        self.assertEqual(length,item.length)
        self.assertEqual(diameter,item.diameter)
        self.assertEqual(weight,item.weight)
    
    def test_create_cylinder_item_with_invalid_length(self):
        with self.assertRaises(Exception):
            item = CylinderItem(0.0,1.0,0.3)
    
    def test_create_cylinder_item_with_invalid_diameter(self):
        with self.assertRaises(Exception):
            item = CylinderItem(5.0,0.0,0.3)

class TestEnvelopeItem(unittest.TestCase):

    def setUp(self):
        pass
    
    def test_create_envelope_item(self):
        width = 1.0
        length = 3.0
        weight = 0.3
        
        item = EnvelopeItem(width,length,weight)
        self.assertEqual(width,item.width)
        self.assertEqual(length,item.length)
        self.assertEqual(weight,item.weight)
    
    def test_create_envelope_item_with_invalid_width(self):
        with self.assertRaises(Exception):
            item = EnvelopeItem(0.0,3.0,0.3)
    
    def test_create_envelope_item_with_invalid_length(self):
        with self.assertRaises(Exception):
            item = EnvelopeItem(1.0,0.0,0.3)

