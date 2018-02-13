# -*- coding: utf-8 -*-

class Item(object):

    def __init__(self, weight):
        if (weight <= 0.0):
            raise Exception('The weight parameter cannot be zero, please specify a value greater than zero')
        
        self.weight = float(weight)

class BoxItem(Item):

    def __init__(self, height, width, depth, weight):
        if (height <= 0.0):
            raise Exception('The height parameter cannot be zero, please specify a value greater than zero')
        elif (width <= 0.0):
            raise Exception('The width parameter cannot be zero, please specify a value greater than zero')
        elif (depth <= 0.0):
            raise Exception('The depth parameter cannot be zero, please specify a value greater than zero')
        
        self.height = float(height)
        self.width = float(width)
        self.depth = float(depth)
        Item.__init__(self,weight)

class CylinderItem(Item):

    def __init__(self, length, diameter, weight):
        if (length <= 0.0):
            raise Exception('The length parameter cannot be zero, please specify a value greater than zero')
        elif (diameter <= 0.0):
            raise Exception('The diameter parameter cannot be zero, please specify a value greater than zero')
        
        self.length = float(length)
        self.diameter = float(diameter)
        self.weight = float(weight)
        Item.__init__(self,weight)

class EnvelopeItem(Item):

    def __init__(self, width, length, weight):
        if (width <= 0.0):
            raise Exception('The width parameter cannot be zero, please specify a value greater than zero')
        elif (length <= 0.0):
            raise Exception('The length parameter cannot be zero, please specify a value greater than zero')
        
        self.width = float(width)
        self.length = float(length)
        self.weight = float(weight)
        Item.__init__(self,weight)
