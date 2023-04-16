#MenuTitle: My Scrambler
__doc__ = """
Create a new tab with a random sequence of selected glyphs.
"""

import random

def myScrambler(num=100):
	glyphs_list = []
	if Font.selectedLayers is None:
		for g in Font.glyphs:
			glyphs_list.append('/' + g.name)
	else:
		for l in Font.selectedLayers:
			glyphs_list.append('/' + l.parent.name)
	glyphs_list = random.choices(glyphs_list, k=num)
	s = ''.join(glyphs_list)
	Font.newTab(s)

myScrambler()
