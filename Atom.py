from typing import List, Tuple, Dict

"""
Contains information about Atoms
Represents a single atom
"""
class Atom():
    names: Dict[str, str] = {
        "H_HOH": "H of water",
        "O_HOH": "O of water",
        "C_UNL": "C of pfoa",
        "F_UNL": "F of pfoa",
        "O_UNL": "O of pfoa",
        "H_UNL": "H of pfoa",
    }
    masses: Dict[str, float] = {
        "H_HOH": 1.0078,
        "O_HOH": 15.9994,
        "C_UNL": 12.011,
        "F_UNL": 18.998403,
        "O_UNL": 15.9994,
        "H_UNL": 1.0078,
    }

    """
    Constructor
    """
    def __init__(self, atom_type: str, position: Tuple[float, float, float]):
        self.type = atom_type
        self.position = position

    """
    Returns atom name from atom type
    """
    @staticmethod
    def get_name(atom_type: str) -> str:
        return Atom.names[atom_type]

    """
    Returns atom mass from atom type
    """
    @staticmethod
    def get_mass(atom_type: str) -> float:
        return Atom.masses[atom_type]
