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
    Extract position from space seperated line representing atom in pdb
    Returns tuple representing position
    """
    @staticmethod
    def get_position(parts: List[str], default_offset: int) -> Tuple[float, float, float]:
        # Default the position_offset to default_offset
        position_offset = default_offset

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

        return atom_pos

    """
    Reads filepath and stores each line in that file
    Returns list of lines in file
    """
    @classmethod
    def read_file(cls, filepath: str) -> List[str]:
        cls.lines = []

        # Open filepath and extract all the lines from the file
        with open(filepath, "r") as file:
            for line in file:
                cls.lines.append(line.strip())

        return cls.lines

    """
    Get the nth line of the file (0 indexed)
    """
    @classmethod
    def get_line(cls, n: int) -> str:
        return cls.lines[n]

    """
    Parse each line in a pdb file and stores a list of atoms
    Returns list of atoms in file
    """
    @classmethod
    def parse(cls) -> List[Atom]:
        cls.atoms = []

        for line in cls.lines:
            # Split each line into parts
            parts = [part.strip() for part in line.split(" ") if part != ""]

            # If the line is not an atom, then ignore the line
            if parts[0] != "HETATM" and parts[0] != "ATOM": continue

            # Default offset is 6, because that's often where it is
            atom_pos = cls.get_position(parts, default_offset=6)
            atom_type = f"{parts[2]}_{parts[3]}"

            atom = Atom(atom_type, atom_pos)
            cls.atoms.append(atom)

        return cls.atoms
    
    """
    Parse poscar_slab.txt
    and stores a list of atoms
    """
    @classmethod
    def parse_poscar(cls) -> None:
        cls.atoms = []

        for line_nr in range(8, len(cls.lines)):
            line: str = cls.lines[line_nr]

            # Split each line into parts
            parts = [part.strip() for part in line.split(" ") if part != ""]

            # Default offset is 0, because that's often where it is
            atom_pos = cls.get_position(parts, default_offset=0)
            atom_type = parts[3]

            atom = Atom(atom_type, atom_pos)
            cls.atoms.append(atom)

        return cls.atoms

    """
    Returns list of atoms
    """
    @classmethod
    def extract(cls) -> List[Atom]:
        return cls.atoms
