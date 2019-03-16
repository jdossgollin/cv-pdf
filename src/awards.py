"""
This script creates the experience tex file
"""

import os
import pandas as pd
from codebase import cventry, get_years

def main():
    data_dir = os.path.join(os.path.dirname(__file__), os.pardir, "data")
    tex_dir = os.path.join(os.path.dirname(__file__), os.pardir, "tex")
    infile = os.path.join(data_dir, "experience.csv")
    outfile = os.path.join(tex_dir, "experience.tex")

    experience = pd.read_csv(infile).fillna("")

    section_text = "\section{Experience}"
    for i,row in experience.iterrows():
        years = get_years(row.syear, row.eyear)
        args = [
            years, row.title, row.institution,
            row.location1, row.location2, row.details
        ]
        item = cventry(args)
        section_text += "\n"
        section_text += item.text

    
    with open(outfile, "w") as f:
        f.write(section_text)

if __name__ == "__main__":
    main()