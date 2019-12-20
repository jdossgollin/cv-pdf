"""
Parse the talks
"""

import os
import yaml

ROOT_DIR = DATA_FILE = os.path.abspath(
    os.path.join(os.path.dirname(__file__), os.pardir)
)
DATA_FILE = os.path.join(ROOT_DIR, "data", "talks.yml")
TEX_FILE = os.path.join(ROOT_DIR, "tex", "talks.tex")

if __name__ == "__main__":
    with open(DATA_FILE, "r") as file:
        talks = yaml.full_load(file)

    talks_ordered = sorted(talks, key=lambda x: x["date"], reverse=True)

    strings = [
        "\cventry"
        + "{"
        + str(talk["date"])
        + "}{"
        + talk["title"]
        + "}{"
        + talk["venue"]
        + "}{"
        + talk["location"]
        + "}{"
        + talk["format"]
        + "}{}\n"
        for talk in talks_ordered
    ]

    with open(TEX_FILE, "w") as file:

        file.write("\subsection{Talks and Workshop Presentations}\n")

        for string in strings:
            file.write(string)
