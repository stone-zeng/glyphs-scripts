#MenuTitle: Clear Layer
# -*- coding: utf-8 -*-
__doc__="""
Clear all paths and components in selected layers.
"""

for layer in Glyphs.font.selectedLayers:
    layer.paths = []
    layer.components = []
