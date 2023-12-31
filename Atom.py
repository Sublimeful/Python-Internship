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
        "Na_UNL": 7,
        "Cl_UNL": 8,

        "Ti": 9,
        "Si": 10,
        "O": 11,
    }

    names: Dict[str, str] = {
        "H_HOH": "H of water",
        "O_HOH": "O of water",
        "C_UNL": "C of pfoa",
        "F_UNL": "F of pfoa",
        "O_UNL": "O of pfoa",
        "H_UNL": "H of pfoa",
        "Na_UNL": "Na of ion",
        "Cl_UNL": "Cl of ion",

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
        "Na_UNL": 22.989769,
        "Cl_UNL": 35.453,

        "Ti": 47.867,
        "Si": 28.0855,
        "O": 15.9994,
    }

    charges: Dict[str, float] = {
        "H_HOH": 0,
        "O_HOH": 0,
        "C_UNL": 0,
        "F_UNL": 0,
        "O_UNL": 0,
        "H_UNL": 0,
        "Na_UNL": 0,
        "Cl_UNL": 0,

        "Ti": 0,
        "Si": 0,
        "O": 0,
    }

    def __init__(self, atom_type: str, position: Tuple[float, float, float], charge = 0.0):
        """
        Constructor for Atom
        @param atom_type type of the atom
        @param position position of the atom
        @returns None
        """
        self.type = atom_type
        self.position = position
        self.charge = charge

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

    @staticmethod
    def get_type(atom_type_index: int) -> str:
        """
        @param atom_type_index
        @returns atom type from type index
        """
        return list(Atom.index.keys())[atom_type_index - 1]

    @staticmethod
    def set_charge(atom_type: str, charge: float) -> None:
        """
        Sets the charge of a type of atom
        @param atom_type
        @param charge
        @returns None
        """
        Atom.charges[atom_type] = charge

    @staticmethod
    def get_charge(atom_type: str) -> float:
        """
        @param atom_type
        @returns atom charge from atom type
        """
        return Atom.charges[atom_type]


