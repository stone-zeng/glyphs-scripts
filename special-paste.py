#MenuTitle: Special Paste
# -*- coding: utf-8 -*-
__doc__="""
Paste copied paths and components into current layers.
"""

# See https://gist.github.com/schriftgestalt/6ef3dda00264486cb479

from Foundation import NSPasteboard, NSString, NSUTF8StringEncoding

GSFormatVersion = 3

pasteboard = NSPasteboard.generalPasteboard()
typeName = pasteboard.availableTypeFromArray_(["Glyphs elements pasteboard type"])

if typeName == "Glyphs elements pasteboard type":
    data = pasteboard.dataForType_(typeName)
    dictionary = NSString.alloc().initWithData_encoding_(data, NSUTF8StringEncoding).propertyList()
    # Glyphs 3
    if "shapes" in dictionary:
        elements = dictionary["shapes"]
        for shapeDict in elements:
            path = GSPath.alloc().initWithDict_format_(shapeDict, GSFormatVersion)
            if path is not None:
                shape = path
            else:
                shape = GSComponent.alloc().initWithDict_format_(shapeDict, GSFormatVersion)
            for layer in Glyphs.font.selectedLayers:
                layer.shapes.append(shape)
    # Glyphs 2
    if "paths" in dictionary:
        elements = dictionary["paths"]
        for pathDict in elements:
            path = GSPath.alloc().initWithPathDict_(pathDict)
            for layer in Glyphs.font.selectedLayers:
                    layer.paths.append(path)
    if "components" in dictionary:
        elements = dictionary["components"]
        for componentDict in elements:
            component = GSComponent.alloc().initWithElementDict_(componentDict)
            for layer in Glyphs.font.selectedLayers:
                    layer.components.append(component)
