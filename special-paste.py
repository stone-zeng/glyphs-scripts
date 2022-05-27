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
    if "shapes" in dictionary:
        elements = dictionary["shapes"]
        for shapeDict in elements:
            path = GSPath.alloc().initWithDict_format_(shapeDict, GSFormatVersion)
            if path is not None:
                shape = path
            else:
                shape = GSComponent.alloc().initWithDict_format_(shapeDict, GSFormatVersion)
            for layer in Glyphs.font.selectedLayers:
                layer.shapes.append(shape.copy())
    if "paths" in dictionary:
        elements = dictionary["paths"]
        for pathDict in elements:
            if Glyphs.font.formatVersion == 3:
                path = GSPath.alloc().initWithDict_format_(pathDict, GSFormatVersion)
            else:
                path = GSPath.alloc().initWithPathDict_(pathDict)
            for layer in Glyphs.font.selectedLayers:
                    layer.paths.append(path.copy())
    if "components" in dictionary:
        elements = dictionary["components"]
        for componentDict in elements:
            if Glyphs.font.formatVersion == 3:
                component = GSComponent.alloc().initWithDict_format_(componentDict, GSFormatVersion)
            else:
                component = GSComponent.alloc().initWithElementDict_(componentDict)
            for layer in Glyphs.font.selectedLayers:
                    layer.components.append(component.copy())
