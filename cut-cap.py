#MenuTitle: Cut Cap
__doc__ = """
Cut the terminal of strokes with a `_cap.cup` glyph.
"""

from Foundation import NSPoint

CAP_SIZE = 100.0
CAP_NAME = "_cap.cup"

for path in Font.selectedLayers[0].paths:
	selected_nodes = [i for i in path.nodes if i.selected]
	if len(selected_nodes) == 2:
		(node0, node1) = tuple(selected_nodes)
		scale = abs(node0.y - node1.y) / CAP_SIZE
		cap = GSHint()
		cap.type = CAP
		cap.name = CAP_NAME
		cap.scale = NSPoint(scale, scale)
		(cap.originNode, cap.targetNode) = (node0, node1)
		Font.selectedLayers[0].hints.append(cap)
