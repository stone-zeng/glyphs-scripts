#MenuTitle: Remove Stroke Ends
__doc__ = """
Remove stroke ends (i.e. 喇叭口).
"""

import math


def removeStrokeEnds(layer: GSLayer):
	print("=>", layer.parent.name, layer.parent.string)
	numStrokeEnds = 0
	for path in layer.paths:
		for n0 in (node for node in path.nodes if node.type != OFFCURVE):
			n1, n2, n3 = n0.nextNode, n0.nextNode.nextNode, n0.nextNode.nextNode.nextNode
			p1, p2, p3 = n0.prevNode, n0.prevNode.prevNode, n0.prevNode.prevNode.prevNode
			for func in (
				_process_横,
				_process_竖,
				_process_弯,
			):
				if func(n0, n1, n2, n3, p1, p2, p3):
					numStrokeEnds += 1
					# n0.selected = True
					break
	for path in layer.paths:
		for n0 in (node for node in path.nodes if node.type != OFFCURVE):
			n1, n2, n3 = n0.nextNode, n0.nextNode.nextNode, n0.nextNode.nextNode.nextNode
			p1, p2, p3 = n0.prevNode, n0.prevNode.prevNode, n0.prevNode.prevNode.prevNode
			for func in (
				# _process_竖_start,
				_process_撇_start,
				_process_提_start,
				_process_stroke_end,
			):
				if func(n0, n1, n2, n3, p1, p2, p3):
					numStrokeEnds += 1
					# n0.selected = True
					break
	if numStrokeEnds:
		print(f"   Remove {numStrokeEnds} stroke ends.")


def _process_横(n0, n1, n2, n3, p1, p2, p3):
	# p0                    <- n3 - n2 - n1 - n0
	# |                                       |
	# n0 - n1 - n2 - n3 ->                    p0
	if _isOffCurve(n1, n2) and _nearHorizontal(n0, n1, n2, n3) and n0.x == p1.x and _isStrokeEnd(n0.x, n3.x):
		n0.y = n1.y = n2.y = n3.y
		return True
	# n0 - p1 - p2 - p3 <-                   n1
	# |                                      |
	# n1                   -> p3 - p2 - p1 - n0
	if _isOffCurve(p1, p2) and _nearHorizontal(n0, p1, p2, p3) and n0.x == n1.x and _isStrokeEnd(n0.x, p3.x):
		n0.y = p1.y = p2.y = p3.y
		return True


def _process_竖(n0, n1, n2, n3, p1, p2, p3):
	# n0 - p1 <-         n3
	# |                  |
	# n1                 n2
	# |                  |
	# n2                 n1
	# |                  |
	# n3         -> p1 - n0
	if _isOffCurve(n1, n2) and _nearVertical(n0, n1, n2, n3) and abs(n0.x - p1.x) > 0 and _isVerticalEnd(n0.y, p1.y) and _isStrokeEnd(n0.y, n3.y) and not p1.y < n0.y < n1.y:
		n0.x = n1.x = n2.x = n3.x
		return True
	# p3         <- n1 - n0
	# |                  |
	# p2                 p1
	# |                  |
	# p1                 p2
	# |                  |
	# n0 - n1 ->         p3
	if _isOffCurve(p1, p2) and _nearVertical(n0, p1, p2, p3) and abs(n0.x - n1.x) > 0 and _isVerticalEnd(n0.y, n1.y) and _isStrokeEnd(n0.y, p3.y) and p2.x == p3.x:
		n0.x = p1.x = p2.x = p3.x
		return True
	#         n1
	#         |
	# -> p1 - n0
	if n1.type == LINE and _nearVertical(n0, n1) and n0.y == p1.y and _isStrokeEnd(n0.y, n1.y):
		n0.x = n1.x
		return True


def _process_弯(n0, n1, n2, n3, p1, p2, p3):
	#        <- n3
	#           |
	#           n2
	#           |
	#           n1
	#           |
	#           n0
	#           |
	#           p1
	#          /
	# -> p3 - p2
	if _isOffCurve(n1, n2, p1, p2) and _nearVertical(n0, n1, n2, n3) and n0.x == p1.x and p2.y == p3.y:
		p1.x = n0.x = n1.x = n2.x = n3.x
		return True


def _process_竖_start(n0, n1, n2, n3, p1, p2, p3):
	if _isOffCurve(n1, n2) and _isVerticalEnd(n0.y, n3.y) and _angle(n0) < 180 and _angle(n3) < 180 and n0.x == p1.x and n3.x == n3.nextNode.x:
		n1.x, n1.y = n0.x, n0.y
		n2.x, n2.y = n3.x, n3.y
		return True


def _process_撇_start(n0, n1, n2, n3, p1, p2, p3):
	if _isOffCurve(n1, n2, p1, p2) and _angle(n0) <= 160 and _distance(n0, p3) <= 25 and n3.x < n0.x and p3.x < n0.x and p3.y < n0.y < n3.y:
		x, y = _intersect(p3.prevNode, p3, n0, n3)
		n0.x = n1.x = p1.x = p2.x = p3.x = x
		n0.y = n1.y = p1.y = p2.y = p3.y = y
		n2.x = n3.x
		n2.y = n3.y
		return True
	if _isOffCurve(p1, p2) and _angle(n0) <= 160 and _distance(n0, p3) <= 25 and n1.x < n0.x and p3.x < n0.x and p3.y < n0.y < n1.y:
		x, y = _intersect(p3.prevNode, p3, n0, n1)
		n0.x = p1.x = p2.x = p3.x = x
		n0.y = p1.y = p2.y = p3.y = y
		return True


def _process_提_start(n0, n1, n2, n3, p1, p2, p3):
	if _isOffCurve(n1, n2, p1, p2) and 40 <= _distance(n0, n3) <= 125 and _distance(n0, p3) <= 60 and _angle(n0) <= 160 and _angle(n3) <= 160 and n0.x < n3.x and n0.x < p3.x and n3.y < n0.y < p3.y:
		x, y = _intersect(p3.prevNode, p3, n0, n3)
		n0.x = n1.x = p1.x = p2.x = p3.x = x
		n0.y = n1.y = p1.y = p2.y = p3.y = y
		return True
	if _isOffCurve(n1, n2, p1, p2) and 40 <= _distance(n0, p3) <= 125 and _distance(n0, n3) <= 60 and _angle(n0) <= 160 and _angle(p3) <= 160 and p3.x < n0.x < n3.x and n0.y < n3.y and n0.y < p3.y:
		x, y = _intersect(n3.nextNode, n3, n0, p3)
		n0.x = n1.x = n2.x = n3.x = p1.x = x
		n0.y = n1.y = n2.y = n3.y = p1.y = y
		return True
	if _isOffCurve(p1, p2) and 40 <= _distance(n0, n1) <= 125 and _distance(n0, p3) <= 85 and _angle(n0) <= 160 and _angle(n1) <= 160 and n0.x < n1.x and n0.x < p3.x and n1.y < n0.y < p3.y:
		x, y = _intersect(p3.prevNode, p3, n0, n1)
		n0.x = p1.x = p2.x = p3.x = x
		n0.y = p1.y = p2.y = p3.y = y
		return True
	if _isOffCurve(n1, n2) and 40 <= _distance(n0, p1) <= 125 and _distance(n0, n3) <= 85 and _angle(n0) <= 160 and _angle(p1) <= 160 and p1.x < n0.x < n3.x and n0.y < n3.y and n0.y < p1.y:
		x, y = _intersect(n3.nextNode, n3, n0, p1)
		n0.x = n1.x = n2.x = n3.x = x
		n0.y = n1.y = n2.y = n3.y = y
		return True


def _process_stroke_end(n0, n1, n2, n3, p1, p2, p3):
	if _isOffCurve(n1, n2) and 40 <= _distance(n0, n3) <= 125 and 0 < _distance(n0, n1) and 0 < _distance(n3, n2) and _angle(n0) <= 160 and _angle(n3) <= 160:
		n1.x, n1.y = n0.x, n0.y
		n2.x, n2.y = n3.x, n3.y
		return True


def _isOffCurve(*nodes: GSNode):
	return all(node.type == OFFCURVE for node in nodes)


def _nearHorizontal(*nodes: GSNode):
	ys = [node.y for node in nodes]
	return 0 < max(ys) - min(ys) <= 3


def _nearVertical(*nodes: GSNode):
	xs = [node.x for node in nodes]
	return 0 < max(xs) - min(xs) <= 3


def _isStrokeEnd(a: float, b: float):
	return abs(a - b) <= 95


def _isVerticalEnd(a: float, b: float):
	return abs(a - b) <= 6


def _distance(node1: GSNode, node2: GSNode):
	return math.sqrt((node1.x - node2.x) ** 2 + (node1.y - node2.y) ** 2)


def _angle(node: GSNode):
	x1, y1 = node.x - node.prevNode.x, node.y - node.prevNode.y
	x2, y2 = node.x - node.nextNode.x, node.y - node.nextNode.y
	s = x1 * x2 + y1 * y2
	d = math.sqrt((x1 ** 2 + y1 ** 2) * (x2 ** 2 + y2 ** 2))
	if math.isclose(d, 0):
		return 0.0
	if abs(s) >= d:
		return math.acos(1 if s > 0 else -1) * 180 / math.pi
	return math.acos(s / d) * 180 / math.pi


def _intersect(node1: GSNode, node2: GSNode, node3: GSNode, node4: GSNode):
	x1, y1 = node1.x, node1.y
	x2, y2 = node2.x, node2.y
	x3, y3 = node3.x, node3.y
	x4, y4 = node4.x, node4.y
	a1, b1, c1 = y2 - y1, -(x2 - x1), (x2 - x1) * y1 - (y2 - y1) * x1
	a2, b2, c2 = y4 - y3, -(x4 - x3), (x4 - x3) * y3 - (y4 - y3) * x3
	return (
		round((b1 * c2 - b2 * c1) / (a1 * b2 - a2 * b1)),
		round((a2 * c1 - a1 * c2) / (a1 * b2 - a2 * b1)),
	)


def cleanUpPaths(layer: GSLayer, n: int = 3):
	for _ in range(n):
		layer.cleanUpPaths()


def main():
	for layer in Font.selectedLayers:
		for path in layer.paths:
			path.selected = False
		removeStrokeEnds(layer)
		cleanUpPaths(layer)


if __name__ == "__main__":
	main()
