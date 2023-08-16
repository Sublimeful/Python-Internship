from typing import List, Tuple, Dict, Any
from Atom import *

class Parser():
    """
    Reads lines from a file, extracts atoms from each line and returns a list of atoms
    Also contains utility functions as well
    """
    lines: List[str] = None
    atoms: List[Atom] = None

    @classmethod
    def read_file(cls, filepath: str) -> List[str]:
        """
        Reads filepath and stores each line in that file
        @params filepath
        @returns list of lines in file
        """
        cls.lines = []

        # Open filepath and extract all the lines from the file
        with open(filepath, "r") as file:
            for line in file:
                cls.lines.append(line.strip())

        return cls.lines

    @classmethod
    def get_line(cls, n: int) -> str:
        """
        Get the nth line of the file (0 indexed)
        @params n
        @returns line
        """
        return cls.lines[n]

    @classmethod
    def clear_atoms(cls):
        """
        Clears the atoms list
        @returns None
        """
        cls.atoms = []

    @classmethod
    def parse_pdb(cls, append = False) -> List[Atom]:
        """
        Parse each line in a pdb file and stores a list of atoms
        @returns list of atoms in file
        """
        if not append:
            cls.atoms = []

        for line in cls.lines:
            # Split each line into parts
            parts = [part.strip() for part in line.split(" ") if part != ""]

            # If the line is empty then continue
            if len(parts) == 0: continue

            # If the line is not an atom, then ignore the line
            if parts[0] != "HETATM" and parts[0] != "ATOM": continue

            # Default offset is 6, because that's often where it is
            atom_pos = cls.get_position(parts, default_offset=6)
            atom_type = f"{parts[2]}_{parts[3]}"

            try:
                # Charge is always preceded by the same value as parts[2]
                atom_charge = float(parts[-1]) if parts[-2] == parts[2] else 0
            except:
                atom_charge = 0

            atom = Atom(atom_type, atom_pos, atom_charge)
            cls.atoms.append(atom)

        return cls.atoms

    @classmethod
    def parse_data(cls, append = False) -> None:
        """
        Parse a data_X.txt file and stores a list of atoms
        @returns None
        """
        if not append:
            cls.atoms = []

        masses_index = cls.lines.index("Masses")
        atoms_index = cls.lines.index("Atoms")

        for line_nr in range(atoms_index + 2, len(cls.lines)):
            line: str = cls.lines[line_nr]

            # Split each line into parts
            parts = [part.strip() for part in line.split(" ") if part != ""]
            # Default offset is 3, because that's often where it is
            atom_pos = cls.get_position(parts, default_offset=3)
            atom_type = Atom.get_type(int(parts[1]))

            atom = Atom(atom_type, atom_pos)
            cls.atoms.append(atom)

    @classmethod
    def parse_poscar(cls, append = False) -> None:
        """
        Parse poscar_slab.txt and stores a list of atoms
        @returns None
        """
        if not append:
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

    @classmethod
    def extract(cls) -> List[Atom]:
        """
        @returns list of atoms
        """
        return cls.atoms

    ###
    ### UTILITY FUNCTIONS
    ###

    @staticmethod
    def get_position(parts: List[str], default_offset: int) -> Tuple[float, float, float]:
        """
        Extract position from space seperated line representing atom in pdb
        @params parts parts of a space deliminated line
        @params default_offset where the algorithm will search first
        @returns tuple representing position
        """
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

    @staticmethod
    def read_input_file(filename: str) -> Dict[str, str]:
        """
        Parses input file
        @param filename name of the input file
        @returns dictionary containing key-value pairs of params
        """
        res = {}
        for line in Parser.read_file(filename):
            s = line.split("#")[0]  # ignore comments
            if s.count("=") != 1: continue  # Ignore lines that start with a # or does not contain exactly one =
            parts = [part.strip() for part in s.split("=") if part != ""]
            res[parts[0]] = parts[1]
        return res
