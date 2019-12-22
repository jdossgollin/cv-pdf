"""
Parse the languages
"""

import os
from typing import Dict
import yaml

from common import ROOT_DIR, make_cvitem, make_subsection

DATA_FILE = os.path.join(ROOT_DIR, "data", "languages.yml")
TEX_FILE = os.path.join(ROOT_DIR, "tex", "languages.tex")


def parse_language(lang: Dict[str, str]) -> str:
    """
    Parse a single talk
    """

    return make_cvitem(arg1=lang["language"], arg2=lang["level"],)


if __name__ == "__main__":
    with open(DATA_FILE, "r") as file:
        languages = yaml.full_load(file)

    strings = [parse_language(language) for language in languages]

    with open(TEX_FILE, "w") as file:

        file.write(make_subsection("Languages"))

        for string in strings:
            file.write(string)
