# fullcv

This is the source files for my CV, built in latex using the `moderncv` template and `biblatex` (via `biber`) for bibliographies. 
The code isn't beautifully written, but it's effective for what it does.
Thanks to the `LaTeX` package authors, Stack Exchange posts, etc.

## Presentations

Since putting presentations into latex format is a bit of a hassle, I have stored them in a separate `.csv` file.
The `make_presentations.py` file parses the `.csv` file and outputs a `.tex` file which can be included in the CV via an `\input{presentations.tex}` command.
To run the python script, you'll need `pandas` and `titlecase`, for example using the environment [here](https://github.com/jdossgollin/jdossgollin.github.io/blob/source/environment.yml) (which is overkill).
One advantage of this tool is that everything is automatically sorted by date, regardless of order in the CSV file.

I should incorporate this into a Makefile eventually...