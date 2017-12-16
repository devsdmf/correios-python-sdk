
# -*- coding: utf-8 -*-

class Package(object):

    FORMAT_BOX      = 1
    FORMAT_CYLINDER = 2
    FORMAT_ENVELOPE = 3

    def __init__(self, format = None):
        self.format = format or self.FORMAT_BOX

        self.set_height()
        self.set_width()
        self.set_length()
        self.set_diameter()

    def get_format(self):
        return self.format

    def set_height(self, height = 0.0):
        self.height = float(height)

    def get_height(self):
        return self.height

    def set_width(self, width = 0.0):
        self.width = float(width)

    def get_width(self):
        return self.width

    def set_length(self, length = 0.0):
        self.length = float(length)

    def get_length(self):
        return self.length

    def set_diameter(self, diameter = 0.0):
        self.diameter = diameter

    def get_diameter(self):
        return self.diameter

    def set_weight(self, weight = 0.0):
        self.weight = weight

    def get_weight(self):
        return self.weight
