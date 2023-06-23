from typing import List, Tuple, Dict
from Atom import *

"""
Reads lines from a file
Extracts atoms from each line and returns a list of atoms
"""
class Parser():
    lines: List[str] = None
    atoms: List[Atom] = None

    """
    Reads filepath and stores
    each line in that file
    """
    @classmethod
    def read_file(cls, filepath: str) -> None:
        cls.lines = []

        # Open filepath and extract all the lines from the file
        with open(filepath, "r") as file:
            for line in file:
                cls.lines.append(line.strip())

        return cls.lines

    """
    Parse each line in the file
    and stores a list of atoms
    """
    @classmethod
    def parse(cls) -> None:
        cls.atoms = []

        for line in cls.lines:
            # Split each line into parts
            parts = [part.strip() for part in line.split(" ") if part != ""]

            # If the line is not an atom, then ignore the line
            if parts[0] != "HETATM": continue

            atom_type = f"{parts[2]}_{parts[3]}"
            atom_pos = (float(parts[6]), float(parts[7]), float(parts[8]))
            atom = Atom(atom_type, atom_pos)
            cls.atoms.append(atom)

        return cls.atoms
    
    """
    Returns list of atoms
    """
    @classmethod
    def extract(cls) -> List[Atom]:
        return cls.atoms
