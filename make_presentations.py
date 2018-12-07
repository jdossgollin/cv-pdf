"""
This file reads in a CSV of presentations and outputs them as well-formatted
latex \cventry files
"""

import pandas as pd
import os

filename = "presentations.csv"
csv = (
    pd.read_csv(
        filename,
        parse_dates=True,
        index_col="date",
        na_values="",
        quotechar='"',
    ).
    fillna('').
    sort_index(ascending=False)
)

outfile = "presentations.tex"
if os.path.isfile(outfile):
    os.remove(outfile)

with open(outfile, "w") as text_file:
    for idx,row in csv.iterrows():
        date =  idx.date().strftime('%Y-%m-%d')
        title = row.title.title()
        event = row.event.title()
        location = row.location
        event_format = row.format.lower()
        string = r"\cventry"
        string += f"{{{date}}}{{{title}}}{{{event}}}{{{location}}}{{{event_format}}}{{}}\n"
        text_file.write(string)

print("All done")
