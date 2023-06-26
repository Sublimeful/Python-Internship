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

        # Default the position_offset to 6
        # because that's often where it is
        position_offset = 6

        for line in cls.lines:
            # Split each line into parts
            parts = [part.strip() for part in line.split(" ") if part != ""]

            # If the line is not an atom, then ignore the line
            if parts[0] != "HETATM" and parts[0] != "ATOM": continue

            atom_type = f"{parts[2]}_{parts[3]}"
            atom_pos = None
            while atom_pos is None:
                # Normalize the position_offset
                position_offset %= len(parts) - 2
                try:
                    x = float(parts[position_offset])
                    y = float(parts[position_offset + 1])
                    z = float(parts[position_offset + 2])
                    atom_pos = (x, y, z)
                except ValueError:
                    # Increase the position_offset
                    position_offset += 1
            atom = Atom(atom_type, atom_pos)
            cls.atoms.append(atom)

        return cls.atoms

    """
    Returns list of atoms
    """
    @classmethod
    def extract(cls) -> List[Atom]:
        return cls.atoms
