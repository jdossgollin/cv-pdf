"""
Parse the talks
"""

import os
from typing import Dict
import yaml

from common import ROOT_DIR, make_cventry, make_subsection

DATA_FILE = os.path.join(ROOT_DIR, "data", "talks.yml")
TEX_FILE = os.path.join(ROOT_DIR, "tex", "talks.tex")


def parse_talk(talk: Dict[str, str]) -> str:
    """
    Parse a single talk
    """

    if "url" in talk.keys():
        talk["format"] = "\href{" + talk["url"] + "}{" + talk["format"] + "}"

    return make_cventry(
        arg1=str(talk["date"]),
        arg2=talk["title"].title(),
        arg3=talk["venue"],
        arg4=talk["location"],
        arg5=talk["format"],
    )


if __name__ == "__main__":
    with open(DATA_FILE, "r") as file:
        talks = yaml.full_load(file)

    talks_ordered = sorted(talks, key=lambda x: x["date"], reverse=True)
    
    # ibid if necessary
    for i in reversed(range(1, len(talks_ordered))):
        if talks_ordered[i]["title"] == talks_ordered[i-1]["title"]:
            talks_ordered[i]["title"] = "ibid"

    strings = [parse_talk(talk) for talk in talks_ordered]

    with open(TEX_FILE, "w") as file:

        file.write(make_subsection("Invited Talks"))

        for string in strings:
            file.write(string)
