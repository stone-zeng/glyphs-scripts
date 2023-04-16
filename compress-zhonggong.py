#MenuTitle: Compress Zhonggong
__doc__="""
Compress Zhonggong (中宫) for CJK characters.
"""

def getCenter(obj):
	center_x = obj.bounds.origin.x + obj.bounds.size.width / 2
	center_y = obj.bounds.origin.y + obj.bounds.size.height / 2
	return center_x, center_y

for layer in Font.selectedLayers:
	layer_center_x, layer_center_y = getCenter(layer)
	for path in layer.paths:
		path_center_x, path_center_y = getCenter(path)
		path.applyTransform([
			1.0, # x scale factor
			0.0, # x skew factor
			0.0, # y skew factor
			1.0, # y scale factor
			0.05 * (layer_center_x - path_center_x), # x position
			0.05 * (layer_center_y - path_center_y)  # y position
		])
