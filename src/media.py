"""
Parse the media
"""

import os
from typing import Dict
import yaml

from common import ROOT_DIR, make_cventry, make_subsection

DATA_FILE = os.path.join(ROOT_DIR, "data", "media.yml")
TEX_FILE = os.path.join(ROOT_DIR, "tex", "media.tex")


def parse_media(media: Dict[str, str]) -> str:
    """
    Parse a single talk
    """

    if media["url"]:
        arg2 = "\href{" + media["url"] + "}{" + media["name"] + "}"
    else:
        arg2 = media["name"]

    return make_cventry(
        arg1=media["date"].__str__(), arg2=arg2, arg3=media["publication"],
    )


if __name__ == "__main__":
    with open(DATA_FILE, "r") as file:
        all_media = yaml.full_load(file)

    media_sorted = sorted(all_media, key=lambda x: x["date"], reverse=True)
    strings = [parse_media(media=media) for media in media_sorted]

    with open(TEX_FILE, "w") as file:

        file.write(make_subsection("Media Coverage"))

        for string in strings:
            file.write(string)
