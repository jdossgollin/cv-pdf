"""
Parse the talks
"""

import os
from typing import Dict
import yaml

from common import ROOT_DIR, make_cventry, make_subsection

DATA_FILE = os.path.join(ROOT_DIR, "data", "conferences.yml")
TEX_FILE = os.path.join(ROOT_DIR, "tex", "conferences.tex")


def parse_conference(conference: Dict[str, str]) -> str:
    """
    Parse a single talk
    """

    return make_cventry(
        arg1=str(conference["date"]),
        arg2=conference["role"],
        arg3=conference["session"],
        arg4=conference["conference"],
        arg5=conference["location"],
    )


if __name__ == "__main__":
    with open(DATA_FILE, "r") as file:
        conferences = yaml.full_load(file)

    conferences_ordered = sorted(conferences, key=lambda x: x["date"], reverse=True)

    strings = [parse_conference(conference) for conference in conferences_ordered]

    with open(TEX_FILE, "w") as file:

        file.write(make_subsection("Conferences and Workshops Organized"))

        for string in strings:
            file.write(string)
