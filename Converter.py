from typing import List, Tuple, Dict
from Atom import *

class Converter():
    """
    Takes a list of Atoms and converts it to a list of strings for output
    """

    class Options():
        """
        A class representing optional parameters for the converter
        """
        def __init__(self, z_max: float = 1_000_000.0):
            self.z_max = z_max

    atoms: List[Atom] = None
    num_of_atoms: int = None
    atom_types: List[str] = None
    output: str = None
    options: Options = Options()

    @classmethod
    def analyze(cls, atoms: List[Atom]) -> None:
        """
        Stores list of atoms, how many atoms there are, and all atom types (SYMBOL_ORIGIN)
        @params atoms list of Atoms
        @returns None
        """

        # Filter atoms according to the options set
        def filter_atoms(atom: Atom) -> bool:
            # Filter atoms that are greater than the z_max
            if atom.position[2] > cls.options.z_max:
                return False

            return True

        cls.atoms = list(filter(filter_atoms, atoms))
        cls.num_of_atoms = len(cls.atoms)
        cls.atom_types = []

        for atom in cls.atoms:
            if atom.type not in cls.atom_types:
                cls.atom_types.append(atom.type)

        # Sort the atom_types array by type index
        cls.atom_types.sort(key=lambda atom_type: Atom.get_index(atom_type))

    @classmethod
    def generate(cls, header: str) -> None:
        """
        Generates output from internal state
        @params header line to put at the top of the output file
        @returns None
        """
        # "Local" mapping from atom type to index
        type_index: Dict[str, int] = {}

        # Result string
        res = []

        # Header
        res.append(header)
        res.append("")

        # Atom information
        padding = len(str(cls.num_of_atoms)) + 1
        res.append(str(cls.num_of_atoms).ljust(padding) + "atoms")
        res.append(str(len(cls.atom_types)).ljust(padding) + "atom types")
        res.append("")
        
        # Atom masses
        padding = 14
        res.append("Masses")
        res.append("")
        for index, atom_type in enumerate(cls.atom_types):
            # Initialize type index
            type_index[atom_type] = index + 1
            s = f"{index + 1} {Atom.get_mass(atom_type)}".ljust(padding) + " ! "
            s += Atom.get_name(atom_type)
            res.append(s)
        res.append("")

        # Atoms
        padding = 7
        res.append("Atoms")
        res.append("")
        for index, atom in enumerate(cls.atoms):
            s = str(index + 1).ljust(padding)
            s += str(type_index[atom.type]).ljust(padding)
            if atom.type == "Na_UNL":
                s += "1".ljust(padding)
            elif atom.type == "Cl_UNL":
                s += "-1".ljust(padding)
            else:
                s += "0".ljust(padding)
            s += " ".join([str(fpos).ljust(padding) for fpos in atom.position])
            res.append(s)

        # Store output
        cls.output = res

    @classmethod
    def extract(cls) -> List[str]:
        """
        @returns list of strings representing output generated
        """
        return cls.output
