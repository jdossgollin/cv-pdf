"""
Parse the talks
"""

import os
import yaml

from common import ROOT_DIR, make_cventry, make_section

DATA_FILE = os.path.join(ROOT_DIR, "data", "awards.yml")
TEX_FILE = os.path.join(ROOT_DIR, "tex", "awards.tex")

if __name__ == "__main__":
    with open(DATA_FILE, "r") as file:
        awards = yaml.full_load(file)

    awards_ordered = sorted(awards, key=lambda x: x["year"], reverse=True)
    for award in awards_ordered:
        for key in award.keys():
            if award[key] is None:
                award[key] = ""

    strings = [
        make_cventry(
            arg1=str(award["year"]),
            arg2=award["title"],
            arg3=award["awarder"],
            arg4=award["institution"],
        )
        for award in awards_ordered
    ]

    with open(TEX_FILE, "w") as file:

        file.write(make_section("Honors and Awards"))

        for string in strings:
            file.write(string)
