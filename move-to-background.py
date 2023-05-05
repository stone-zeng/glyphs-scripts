#MenuTitle: Move to Background
__doc__ = """
Move certain smart components to Background.
"""

import copy

def main():
	for glyph in (l.parent for l in Font.selectedLayers if not l.parent.name.startswith("_part.Pratyaya")):
		for layer in (l for l in glyph.layers if " at " not in l.name):
			indices = []
			for i, shape in enumerate(layer.shapes):
				if shape.shapeType == GSShapeTypeComponent and shape.name.startswith("_part.Pratyaya"):
					indices.append(i)
					layer.background.shapes.append(copy.deepcopy(shape))
					print(layer, shape)
			if indices:
				for i in reversed(indices):
					del(layer.shapes[i])

main()
