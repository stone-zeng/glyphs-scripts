#MenuTitle: Shuffle Text
# -*- coding: utf-8 -*-
__doc__="""
Shuffle the preview text.
"""

import random

tab = Glyphs.font.currentTab
layers = list(tab.layers)
random.shuffle(layers)
tab.layers = layers
