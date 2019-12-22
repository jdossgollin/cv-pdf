"""
Parse the outreach
"""

import os
from typing import Dict, List, Union
import yaml

from common import ROOT_DIR, make_cventry, make_subsection

DATA_FILE = os.path.join(ROOT_DIR, "data", "outreach.yml")
TEX_FILE = os.path.join(ROOT_DIR, "tex", "outreach.tex")


if __name__ == "__main__":
    with open(DATA_FILE, "r") as file:
        outreach = yaml.full_load(file)

    output = [make_subsection("Outreach and Volunteering")]

    for position in outreach:
        if "eyear" in position.keys():
            position["sortyear"] = position["eyear"]
        else:
            position["sortyear"] = 9999

    outreach_sorted = sorted(outreach, key=lambda x: x["sortyear"], reverse=True)

    for position in outreach_sorted:
        year = ""
        if "eyear" in position.keys():
            if position["syear"] == position["eyear"]:
                year = str(position["eyear"])
            else:
                year = str(position["syear"]) + "--" + str(position["eyear"])
        else:
            year = str(position["syear"]) + "--" + "Present"

        output.append(
            make_cventry(
                arg1=year,
                arg2=str(position["position"]),
                arg3=str(position["organization"]),
                arg4=str(position["institution"]),
                arg5=str(position["location"]),
                arg6=position["description"],
            )
        )

    with open(TEX_FILE, "w") as file:

        for string in output:
            file.write(string)
