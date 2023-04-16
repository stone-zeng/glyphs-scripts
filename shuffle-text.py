#MenuTitle: Shuffle Text
__doc__ = """
Shuffle the preview text.
"""

import random

tab = Font.currentTab
layers = list(tab.layers)
random.shuffle(layers)
tab.layers = layers
