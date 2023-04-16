#MenuTitle: Clear Layer
__doc__ = """
Clear all paths and components in selected layers.
"""

try:
	for layer in Font.selectedLayers:
		layer.shapes = []
except:
	for layer in Font.selectedLayers:
		layer.paths = []
		layer.components = []
