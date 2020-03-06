"""
Parse the media
"""

import os
from typing import Dict
import yaml

from common import ROOT_DIR, make_cventry, make_subsection

DATA_FILE = os.path.join(ROOT_DIR, "data", "public.yml")
TEX_FILE = os.path.join(ROOT_DIR, "tex", "public.tex")


def parse_public(public: Dict[str, str]) -> str:
    """
    Parse a single talk
    """

    if public["url"]:
        arg2 = "\href{" + public["url"] + "}{" + public["name"] + "}"
    else:
        arg2 = public["name"]

    return make_cventry(
        arg1=public["date"].__str__(), arg2=arg2, arg3=public["venue"],
    )


if __name__ == "__main__":
    with open(DATA_FILE, "r") as file:
        all_public = yaml.full_load(file)

    public_sorted = sorted(all_public, key=lambda x: x["date"], reverse=True)
    strings = [parse_public(public=public) for public in public_sorted]

    with open(TEX_FILE, "w") as file:

        file.write(make_subsection("Public Presentations"))

        for string in strings:
            file.write(string)
