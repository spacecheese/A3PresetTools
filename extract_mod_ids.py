#!/usr/bin/env python3

import modset_common as common
import argparse

parser = argparse.ArgumentParser(
    prog="extract_mod_ids.py",
    usage="%(prog)s [preset] [options]",
    description="Reads a presets the mod ids to a file.",
)
parser.add_argument("preset")
parser.add_argument(
    "-o",
    "--output",
    help="file to write mod ids to (defaults to mods.txt)",
    default="mods.txt",
)
args = parser.parse_args()

preset = common.ModSet.from_preset(args.preset)

modIds = ""
for mod in preset.mods:
    modIds += str(mod.id) + "\n"

outputPath = args.output
if outputPath is None:
    outputPath = "mods.txt"

with open(outputPath, "w") as f:
    f.write(modIds)