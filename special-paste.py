#MenuTitle: Special Paste
# -*- coding: utf-8 -*-
__doc__="""
Paste copied paths and components into current layers.
"""

# See https://gist.github.com/schriftgestalt/6ef3dda00264486cb479

from Foundation import *

pasteboard = NSPasteboard.generalPasteboard()
typeName = pasteboard.availableTypeFromArray_(["Glyphs elements pasteboard type"])

if typeName == "Glyphs elements pasteboard type":
    data = pasteboard.dataForType_(typeName)
    dictionary = NSString.alloc().initWithData_encoding_(data, NSUTF8StringEncoding).propertyList()
    if "paths" in dictionary:
        elements = dictionary["paths"]
        for layer in Glyphs.font.selectedLayers:
            for pathDict in elements:
                path = GSPath.alloc().initWithPathDict_(pathDict)
                layer.paths.append(path)
    if "components" in dictionary:
        elements = dictionary["components"]
        for layer in Glyphs.font.selectedLayers:
            for componentDict in elements:
                component = GSComponent.alloc().initWithElementDict_(componentDict)
                layer.components.append(component)
