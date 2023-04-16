# Glyphs Scripts

Python scripts for use with the [Glyphs font editor](https://glyphsapp.com/).

## Installation

> 1. Put the scripts folder (or an alias) into the *Scripts* folder which appears when you choose
> *Script > Open Scripts Folder* (Cmd-Shift-Y): `~/Library/Application Support/Glyphs 3/Scripts/`
> 2. Then, hold down the Option (Alt) key, and choose *Script > Reload Scripts* (Cmd-Opt-Shift-Y).
> Now the scripts are visible in the *Script* menu
> 3. For some of the scripts, you will also need to install Tal Leming's *Vanilla*: Go to
> *Glyphs > Preferences > Addons > Modules* and click the *Install Modules* button. That’s it.
>
> *From [mekkablue/Glyphs-Scripts](https://github.com/mekkablue/Glyphs-Scripts)*

## About the scripts

- `clear-layer.py`: Clear all paths and components in selected layers.
- `compress-zhonggong.py`: Compress Zhonggong (中宫) for CJK characters.
- `cut-cap.py`: Cut the terminal of strokes with a `_cap.cup` glyph.
- `generate-samples.py`: Generate sample text of certain rules.
- `my-scrambler.py`: Create a new tab with a random sequence of selected glyphs.
- `print-nodes.py`: Print nodes into Wolfram Language format.
- `rvs-circle-scaling.py`: Make the scaled circles round again (for 基本美术体).
- `shuffle-text`: Shuffle the preview text.
- `special-paste.py`: Paste copied paths and components into current layers.

## References

- Tutorials - Scripting Glyphs:
  - [Part 1](https://glyphsapp.com/tutorials/scripting-glyphs-part-1)
  - [Part 2](https://glyphsapp.com/tutorials/scripting-glyphs-part-2)
  - [Part 3](https://glyphsapp.com/tutorials/scripting-glyphs-part-3)
  - [Part 4](https://glyphsapp.com/tutorials/scripting-glyphs-part-4)
- [Glyphs.app Python Scripting API Documentation](https://docu.glyphsapp.com)

## License

Copyright (C) 2020&ndash;2023 by Xiangdong Zeng.

Licensed under the MIT License.
