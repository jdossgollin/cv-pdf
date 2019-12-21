"""
Parse the talks
"""

import os
import yaml

from common import ROOT_DIR, make_cventry, make_section

DATA_FILE = os.path.join(ROOT_DIR, "data", "education.yml")
TEX_FILE = os.path.join(ROOT_DIR, "tex", "education.tex")


if __name__ == "__main__":
    with open(DATA_FILE, "r") as file:
        education = yaml.full_load(file)

    output = [make_section("Education")]

    for position in education:
        if "eyear" in position.keys():
            position["sortyear"] = position["eyear"]
        else:
            position["sortyear"] = 9999

    education_sorted = sorted(education, key=lambda x: x["sortyear"], reverse=True)

    for position in education_sorted:
        if "description" in position.keys():
            description = position["description"]
        else:
            description = ""
        output.append(
            make_cventry(
                arg1=str(position["year"]),
                arg2=str(position["degree"]),
                arg3=str(position["department"]),
                arg4=str(position["university"]),
                arg5=str(position["location"]),
                arg6=description,
            )
        )

    with open(TEX_FILE, "w") as file:

        for string in output:
            file.write(string)
