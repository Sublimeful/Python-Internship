"""
Contains information about Atoms
Represents a single atom
"""
class Atom():
    index: dict[str, int] = {
        "H_HOH": 1,
        "O_HOH": 2,
        "C_UNL": 3,
        "F_UNL": 4,
        "O_UNL": 5,
        "H_UNL": 6,

        "Si": 101,
        "O": 102,
    }
    names: dict[str, str] = {
        "H_HOH": "H of water",
        "O_HOH": "O of water",
        "C_UNL": "C of pfoa",
        "F_UNL": "F of pfoa",
        "O_UNL": "O of pfoa",
        "H_UNL": "H of pfoa",

        "Si": "Silicon",
        "O": "Oxygen",
    }
    masses: dict[str, float] = {
        "H_HOH": 1.0078,
        "O_HOH": 15.9994,
        "C_UNL": 12.011,
        "F_UNL": 18.998403,
        "O_UNL": 15.9994,
        "H_UNL": 1.0078,

        "Si": 28.0855,
        "O": 15.9994,
    }

    """
    Constructor
    """
    def __init__(self, atom_type: str, position: tuple[float, float, float]):
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

    """
    Returns type index from atom type
    """
    @staticmethod
    def get_index(atom_type: str) -> int:
        return Atom.index[atom_type]
