"""
Define some useful codes
"""

"""
Define codes to write the different formats to file
"""

from typing import List

class cventry:
    """
    A cventry has six fields and is printed to multiple lines
    """
    def __init__(self, args: List[str]) -> None:
        """
        Initialize with six arguments
        """
        assert len(args) <= 6, "cannot have more than six args"
        self.args = ["", "", "", "", "", ""]
        for i,arg in enumerate(args):
            self.args[i] = arg
        self.text = f"\cventry"
        for arg in self.args:
            self.text = self.text + "{" + arg + "}"

class cvitem:
    """
    A cvitem has just two fields
    """
    def __init__(self, args: List[str]) -> None:
        """
        Initialize with two arguments
        """
        assert len(args) <= 2, "cannot have more than two args"
        self.args = ["", ""]
        for i,arg in enumerate(args):
            self.args[i] = arg
        self.text = "\cvitem"
        for arg in myargs:
            self.text = self.text + "{" + arg + "}"

class itemized:
    """
    let's also abstract away bullet points
    """
    def __init__(self, args: List[str]) -> None:
        """
        Initialize the itemized list
        """
        self.args = args
        self.text = "\\begin{itemize}"
        for arg in args:
            self.text += "\n\t\\item {}".format(arg)
            
        self.text += "\n\\end{itemize}"
        
def get_years(syear: int, eyear: int):
    """
    convert from a syear and eyear to years
    """
    syear = int(syear)
    if syear == eyear:
        year = f"{syear:d}"
    elif eyear == "":
        year = f"{syear:d}--Present"
    elif eyear > syear:
        eyear = int(eyear)
        year = f"{syear:d}--{eyear:d}"
    else:
        raise ValueError("Invalid years given")
    return year