from typing import List, Tuple, Dict

class Atom():
    """
    Contains information about Atoms
    Represents a single atom
    """

    index: Dict[str, int] = {
        "H_HOH": 1,
        "O_HOH": 2,
        "C_UNL": 3,
        "F_UNL": 4,
        "O_UNL": 5,
        "H_UNL": 6,

        "Ti": 100,
        "Si": 101,
        "O": 102,
    }

    names: Dict[str, str] = {
        "H_HOH": "H of water",
        "O_HOH": "O of water",
        "C_UNL": "C of pfoa",
        "F_UNL": "F of pfoa",
        "O_UNL": "O of pfoa",
        "H_UNL": "H of pfoa",

        "Ti": "Titanium",
        "Si": "Silicon",
        "O": "Oxygen",
    }

    masses: Dict[str, float] = {
        "H_HOH": 1.0078,
        "O_HOH": 15.9994,
        "C_UNL": 12.011,
        "F_UNL": 18.998403,
        "O_UNL": 15.9994,
        "H_UNL": 1.0078,

        "Ti": 47.867,
        "Si": 28.0855,
        "O": 15.9994,
    }

    def __init__(self, atom_type: str, position: Tuple[float, float, float]):
        """
        Constructor for Atom
        @param atom_type type of the atom
        @param position position of the atom
        @returns None
        """
        self.type = atom_type
        self.position = position

    @staticmethod
    def get_name(atom_type: str) -> str:
        """
        @param atom_type
        @returns atom name from atom type
        """
        return Atom.names[atom_type]

    @staticmethod
    def get_mass(atom_type: str) -> float:
        """
        @param atom_type
        @returns atom mass from atom type
        """
        return Atom.masses[atom_type]

    @staticmethod
    def get_index(atom_type: str) -> int:
        """
        @param atom_type
        @returns type index from atom type
        """
        return Atom.index[atom_type]




