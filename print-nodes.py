#MenuTitle: Clear Layer
# -*- coding: utf-8 -*-
__doc__="""
Print nodes into Wolfram Language format.
"""

s0 = '{'
for char in Glyphs.font.selectedLayers:
    s1 = '{'
    for path in char.paths:
        s2 = '{'
        index = 0
        for node in path.nodes:
            point = '{{{},{}}}'.format(node.x, node.y)
            index += 1
            s2 += '<|"Point"->{},"Type"->"{}","Index"->{}|>,'.format(point, node.type, index)
        s2 = s2[:-1] + '},'
        s1 += s2
    s1 = s1[:-1] + '},'
    s0 += s1
s0 = s0[:-1] + '}'
print(s0)
