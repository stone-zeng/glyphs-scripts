#MenuTitle: Print nodes
__doc__ = """
Print nodes into Wolfram Language format.
"""

s0 = "{"
for char in Font.selectedLayers:
	s1 = "{"
	for path in char.paths:
		s2 = "{"
		index = 0
		for node in path.nodes:
			point = f"{{{node.x},{node.y}}}"
			index += 1
			s2 += f"<|\"Point\"->{point},\"Type\"->\"{node.type}\",\"Index\"->{index}|>,"
		s2 = s2[:-1] + "},"
		s1 += s2
	s1 = s1[:-1] + "},"
	s0 += s1
s0 = s0[:-1] + "}"
print(s0)
