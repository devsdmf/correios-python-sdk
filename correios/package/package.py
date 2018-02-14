# -*- coding: utf-8 -*-

from functools import reduce
from . import BoxItem, CylinderItem, EnvelopeItem

class Package(object):

    FORMAT_BOX      = 1
    FORMAT_CYLINDER = 2
    FORMAT_ENVELOPE = 3

    def __init__(self, format = None):
        self.format = format or self.FORMAT_BOX
        self.items = []

    def get_format(self):
        return self.format
    
    def is_format(self, format):
        return True if self.format is format else False

    def add_item(self):
        raise NotImplementedError
    
    def has_items(self): 
        return True if len(self.items) > 0 else False

    def get_items(self):
        return self.items
    
    def get_dimensions(self):
        raise NotImplementedError
    
    def get_weight(self):
        return reduce(lambda s,i: s + i.weight, self.items, 0)
    
    def is_valid(self):
        raise NotImplementedError
    
    def api_format(self):
        raise NotImplementedError

class BoxPackage(Package):

    MIN_HEIGHT = 2.0
    MIN_WIDTH  = 11.0
    MIN_DEPTH  = 16.0
    MAX_HEIGHT = 105.0
    MAX_WIDTH  = 105.0
    MAX_DEPTH  = 105.0
    MAX_VOLUME = 200.0

    def __init__(self):
        Package.__init__(self,Package.FORMAT_BOX)
    
    def add_item(self, height, width, depth, weight):
        return self.items.append(BoxItem(height,width,depth,weight))
    
    def get_dimensions(self):
        items = []

        for item in self.items:
            dimensions = sorted([item.height,item.width,item.depth])
            items.append(BoxItem(
                height=dimensions[0],
                width=dimensions[1],
                depth=dimensions[2],
                weight=item.weight
            ))

        shadow = {
            'height': max(list(map(lambda i: i.height, items)) + [self.MIN_HEIGHT]),
            'width': max(list(map(lambda i: i.width, items)) + [self.MIN_WIDTH]),
            'depth': max(list(map(lambda i: i.depth, items)) + [self.MIN_DEPTH])
        }

        dimension = [k for k,v in shadow.items() if v==min(shadow.values())][0]
        accumulator = reduce(lambda s,i: s + getattr(i,dimension),items,0)
        shadow[dimension] = accumulator if accumulator > shadow[dimension] else shadow[dimension]

        return (shadow['height'],shadow['width'],shadow['depth'])
    
    def is_valid(self):
        height, width, depth = self.get_dimensions()
        volume = height + width + depth

        return True if height <= self.MAX_HEIGHT and width <= self.MAX_WIDTH \
                    and depth <= self.MAX_DEPTH and volume <= self.MAX_VOLUME else False
    
    def api_format(self):
        if self.is_valid():
            height, width, depth = self.get_dimensions()
            return {
                'nCdFormato': self.get_format(),
                'nVlAltura': height,
                'nVlLargura': width,
                'nVlComprimento': depth,
                'nVlPeso': self.get_weight()
            }
        else:
            raise Exception('The current package is not a valid package due to some validation constraints')

class CylinderPackage(Package):

    MIN_LENGTH   = 18.0
    MIN_DIAMETER = 5.0
    MAX_LENGTH   = 105.0
    MAX_DIAMETER = 91.0
    MAX_VOLUME   = 200.0

    def __init__(self):
        Package.__init__(self,Package.FORMAT_CYLINDER)

    def add_item(self, length, diameter, weight):
        return self.items.append(CylinderItem(length,diameter,weight))
    
    def get_dimensions(self):
        diameter = max(list(map(lambda i: i.diameter, self.items)) + [self.MIN_DIAMETER])
        length = max([reduce(lambda s,i: s + i.length, self.items, 0),self.MIN_LENGTH])
        return (length,diameter)
    
    def is_valid(self):
        length, diameter = self.get_dimensions()
        volume = length + (2 * diameter)

        return True if length <= self.MAX_LENGTH and diameter <= self.MAX_DIAMETER \
                    and volume <= self.MAX_VOLUME else False
    
    def api_format(self):
        if self.is_valid():
            length, diameter = self.get_dimensions()
            return {
                'nCdFormato': self.get_format(),
                'nVlComprimento': length,
                'nVlDiametro': diameter,
                'nVlPeso': self.get_weight()
            }
        else:
            raise Exception('The current package is not a valid package due to some validation constraints')

class EnvelopePackage(Package):

    MIN_WIDTH = 11.0
    MIN_LENGTH = 16.0
    MAX_WIDTH = 60.0
    MAX_LENGTH = 60.0
    MAX_WEIGHT = 1.0

    def __init__(self):
        Package.__init__(self,Package.FORMAT_ENVELOPE)
    
    def add_item(self, width, length, weight):
        return self.items.append(EnvelopeItem(width,length,weight))
    
    def get_dimensions(self):
        width = max(list(map(lambda i: i.width, self.items)) + [self.MIN_WIDTH])
        length = max(list(map(lambda i: i.length, self.items)) + [self.MIN_LENGTH])
        return (width, length)
    
    def is_valid(self):
        width, length = self.get_dimensions()
        weight = self.get_weight()
        return True if width <= self.MAX_WIDTH and length <= self.MAX_LENGTH \
                    and weight <= self.MAX_WEIGHT else False
    
    def api_format(self):
        if self.is_valid():
            width, length = self.get_dimensions()
            return {
                'nCdFormato': self.get_format(),
                'nVlAltura': 0.0,
                'nVlLargura': width,
                'nVlComprimento': length,
                'nVlPeso': self.get_weight()
            }
        else:
            raise Exception('The current package is not a valid package due to some validation constraints')
