#MenuTitle: Find Unused Smart Components

smartComponent = set()
usedSmartComponent = set()

for glyph in Font.glyphs:
	if glyph.smartComponentAxes and glyph.name:
		smartComponent.add(glyph.name)
	for layer in glyph.layers:
		for component in layer.components:
			if component.smartComponentValues:
				usedSmartComponent.add(component.name)

for name in sorted(smartComponent - usedSmartComponent):
	print(name)
