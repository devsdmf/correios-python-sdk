
# -*- coding: utf-8 -*-

class Package(object):

    FORMAT_BOX      = 1
    FORMAT_CYLINDER = 2
    FORMAT_ENVELOPE = 3

    def __init__(self, format = self.FORMAT_BOX):
        self.format = format
        set_height()
        set_width()
        set_length()

    def get_format():
        return self.format

    def set_height(height = 0.0):
        self.height = float(height)

    def get_height():
        return self.height

    def set_width(width = 0.0):
        self.width = float(width)

    def get_width():
        return self.width

    def set_length(length = 0.0):
        self.length = float(length)

    def get_length():
        return self.length

    def set_diameter(diameter = 0.0):
        self.diameter = diameter

    def get_diameter():
        return self.diameter

    def set_weight(weight = 0.0):
        self.weight = weight

    def get_weight():
        return self.weight
