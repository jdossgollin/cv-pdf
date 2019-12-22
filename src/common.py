"""
Common utilities
"""

import os
from typing import List, Union

ROOT_DIR = DATA_FILE = os.path.abspath(
    os.path.join(os.path.dirname(__file__), os.pardir)
)


def make_cventry(
    arg1: str = "",
    arg2: str = "",
    arg3: str = "",
    arg4: str = "",
    arg5: str = "",
    arg6: Union[List, str] = "",
) -> str:
    """
    Make the \cventry{}{}{}{}{}{} command
    """

    if isinstance(arg6, str):
        description = arg6
    elif isinstance(arg6, List):
        description = "\\begin{itemize}"
        for arg in arg6:
            description += "\n\t\item " + arg
        description += "\n\\end{itemize}"
    else:
        raise ValueError("description must be string or list")

    string = (
        "\cventry{"
        + arg1
        + "}{"
        + arg2
        + "}{"
        + arg3
        + "}{"
        + arg4
        + "}{"
        + arg5
        + "}{"
        + description
        + "}\n\n"
    )
    return string


def make_cvitem(arg1: str, arg2: str) -> str:
    """
    Make the \cvitem{}{} command
    """

    string = "\cvitem{" + arg1 + "}{" + arg2 + "}\n\n"
    return string


def make_section(name: str) -> str:
    """
    Print the section name in proper format
    """
    return "\section{" + name + "}"


def make_subsection(name: str) -> str:
    """
    Print the subsection name in proper format
    """
    return "\subsection{" + name + "}"
