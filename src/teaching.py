"""
Parse the talks
"""

import os
from typing import Dict, List, Union
import yaml

from common import ROOT_DIR, make_cventry, make_section, make_subsection

DATA_FILE = os.path.join(ROOT_DIR, "data", "teaching.yml")
TEX_FILE = os.path.join(ROOT_DIR, "tex", "teaching.tex")


if __name__ == "__main__":
    with open(DATA_FILE, "r") as file:
        teaching = yaml.full_load(file)

    output = [make_section("Teaching Experience")]

    for university in teaching:
        output.append(make_subsection(university))
        courses_sorted = sorted(
            teaching[university], key=lambda x: x["year"], reverse=True
        )
        for course in courses_sorted:
            output.append(
                make_cventry(
                    arg1=str(course["year"]),
                    arg2=str(course["role"]),
                    arg3=str(course["course"]),
                    arg6=course["description"],
                )
            )

    with open(TEX_FILE, "w") as file:

        for string in output:
            file.write(string)
