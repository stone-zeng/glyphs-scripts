import random

tab = Glyphs.font.currentTab
layers = list(tab.layers)
random.shuffle(layers)
tab.layers = layers
