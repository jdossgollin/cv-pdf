"""
Parse the talks
"""

import os
import yaml

ROOT_DIR = DATA_FILE = os.path.abspath(
    os.path.join(os.path.dirname(__file__), os.pardir)
)
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
        "\cventry"
        + "{"
        + str(award["year"])
        + "}{"
        + award["title"]
        + "}{"
        + award["awarder"]
        + "}{"
        + award["institution"]
        + "}{}{}\n"
        for award in awards_ordered
    ]

    with open(TEX_FILE, "w") as file:

        file.write("\section{Honors \& Awards}\n")

        for string in strings:
            file.write(string)
