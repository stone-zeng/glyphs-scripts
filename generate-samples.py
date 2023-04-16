#MenuTitle: Generate Samples
__doc__ = """
Generate sample text of certain rules.
"""

import re

START_TEXT = "国包发酬夏永婆怅意我持病摂今暖東松随乐家建级虎浅然气的眼街阐"
END_TEXT = "東持国怅今暖像我酬包永夏到妈影怫冬敦爆发意病摂瓣福答細蘭风鷹"

SMART_COMPONENT_PATTERN = re.compile(r"^_part\..+(\d)$")

REPLACE_TEMPLATE = """\
国..我..持...永...暖\
我...松...永..眼..意\
持..然..国...我...持\
永...暖...我..松..永\
眼..意..持...然...国\
"""

NUM_MAX_INTER_LAYER = 50
LINE_LENGTH = 15
NUM_LINE = 9

def main():
	tabLayers = []
	weights = ["Thin", "Regular", "Heavy"]
	for n, weight in enumerate(weights):
		weightId = next(m for m in Font.masters if m.name == weight).id
		layers = generateLayers(weightId)
		tabLayers.extend(layers)
		if n == len(weights) - 1:
			break
		for _ in range(NUM_LINE - (len(layers) % (NUM_LINE * LINE_LENGTH) // LINE_LENGTH)):
			tabLayers.append(GSControlLayer(10))
	tab = Font.newTab()
	tab.layers = tabLayers

def generateLayers(weightId: str):
	layers = []
	for group in generateInterLayerGroups(weightId):
		for c in START_TEXT:
			glyph = findGlyph(c)
			layers.append(glyph.layers[weightId])
		layers.extend(group)
		for c in END_TEXT:
			glyph = findGlyph(c)
			layers.append(glyph.layers[weightId])
	return layers

def generateInterLayerGroups(weightId: str) -> list[list]:
	interLayers = expandLayers(weightId)
	numPage = (len(interLayers) + 1) // NUM_MAX_INTER_LAYER + 1
	groups = []
	i = 0
	for n in range(numPage):
		groups.append([])
		for c in REPLACE_TEMPLATE:
			if c == ".":
				if i >= len(interLayers):
					return groups
				groups[n].append(interLayers[i])
				i += 1
			else:
				glyph = findGlyph(c)
				groups[n].append(glyph.layers[weightId])

def expandLayers(weightId: str):
	layers = []

	def _appendSmartComponets(glyph, name):
		for layer in glyph.layers:
			if layer.associatedMasterId == weightId and (layer.isMasterLayer or layer.name == name):
					layers.append(layer)

	for selectedLayer in Font.selectedLayers or []:
		glyph = selectedLayer.parent
		if match := SMART_COMPONENT_PATTERN.match(glyph.name):
			if match[1] in ("1", "2"):
				_appendSmartComponets(glyph, "Narrow")
				continue
			if match[1] in ("3", "4"):
				_appendSmartComponets(glyph, "Short")
				continue
		layers.append(glyph.layers[weightId])

	return layers

def findGlyph(c: str):
	for glyph in Font.glyphs:
		if glyph.string == c:
			return glyph
	for glyph in Font.importedGlyphs() or []:
		if glyph.string == c:
			return glyph
	return None

main()
