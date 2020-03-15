#MenuTitle: Paste path
# -*- coding: utf-8 -*-
__doc__="""
Paste copied path into current layers.
"""

# See https://gist.github.com/schriftgestalt/6ef3dda00264486cb479

from Foundation import *

pasteboard = NSPasteboard.generalPasteboard()
typeName = pasteboard.availableTypeFromArray_(["Glyphs elements pasteboard type"])

if typeName == "Glyphs elements pasteboard type":
  data = pasteboard.dataForType_(typeName)
  elements = NSString.alloc().initWithData_encoding_(data, NSUTF8StringEncoding).propertyList()["paths"]
  for layer in Glyphs.font.selectedLayers:
    for pathDict in elements:
      path = GSPath.alloc().initWithPathDict_(pathDict)
      layer.paths.append(path)
