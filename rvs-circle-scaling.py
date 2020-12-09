#MenuTitle: RVS Circle Scaling
# -*- coding: utf-8 -*-
__doc__="""
Make the scaled circles round again (RVS).
"""

SCALE_RATIO = 0.7

def isCircle(path):
    if not path.closed or len(path.nodes) != 12:
        return False
    if len([i for i in path.nodes if i.type is 'curve' and i.smooth]) != 4:
        return False
    if len([i for i in path.nodes if i.type is 'offcurve']) != 8:
        return False
    return True

for layer in Glyphs.font.selectedLayers:
    for path in layer.paths:
        if isCircle(path):
            width = path.bounds.size.width
            height = path.bounds.size.height
            x = path.bounds.origin.x + width / 2
            y = path.bounds.origin.y + height / 2
            rx = height / width * SCALE_RATIO
            ry = SCALE_RATIO
            path.applyTransform((
                rx,           # x scale factor
                0.0,          # x skew factor
                0.0,          # y skew factor
                ry,           # y scale factor
                (1 - rx) * x, # x position
                (1 - ry) * y, # y position
            ))
