# Import pymatgen dependancies
#from pymatgen.core.surface import SlabGenerator, Structure, ReconstructionGenerator
#from pymatgen.io.vasp.inputs import Poscar
### shafigh
from typing import List, Tuple, Dict
import sys
sys.path.insert(1, '/usr/local/anaconda3/lib/python3.7/site-packages/')
from pymatgen.core.surface import SlabGenerator, Structure, ReconstructionGenerator
from pymatgen.io.vasp.inputs import Poscar
###
from Atom import *

class Generator():
    """
    Utility class that specializes in write operations
    """

    @staticmethod
    def multiline_strip(s: str) -> str:
        """
        Strips a multiline string on every newline
        @param s the multiline string
        """
        return "\n".join(map(lambda line: line.strip(), s.split("\n")))

    @staticmethod
    def write(filepath: str, s: str) -> None:
        """
        Writes string s to filepath
        @params filepath output file path
        @params s string to write
        @returns None
        """
        with open(filepath, "w+") as file:
            file.write(s)
            file.close()

    @staticmethod
    def write_lines(filepath: str, lines: List[str]) -> None:
        """
        Writes newline separated strings to filepath
        @params filepath output file path
        @params lines list of lines to write
        @returns None
        """
        with open(filepath, "w+") as file:
            file.write("\n".join(lines))
            file.close()

    @staticmethod
    def make_slab(cif_filename: str, slab_dimension: List) -> None:
        """
        Generates poscar_slab.txt from slab_dimension using TiO2_rutile.cif
        @params cif_filename name of the cif file
        @params slab_dimension list of integers specifying slab dimensions
        @returns None
        """

        ### Slab generator code ###
        ### by Srishyam Raghavan (02/17/2020) ###

        structure = Structure.from_file(f"{cif_filename}")   # import Structure before= this
        ##structure = Structure.from_file(f"{cif_filename}.cif")   # import Structure before= this
        ##slab = SlabGenerator(structure,(1,1,0),4,25,center_slab=True)  # 2nd is (h,k,l); 3rd is minimum size of layers containing atoms; 4th is minimum vacuum size (both in angstrom)
        slab = SlabGenerator(structure,(1,0,0),9,25,lll_reduce=True)  # 2nd is (h,k,l); 3rd is minimum size of layers containing atoms; 4th is minimum vacuum size (both in angstrom)
        #slabgen = SlabGenerator(structure, (1,1,0), 3, 25, lll_reduce=True)  # 2nd is (h,k,l); 3rd is minimum size of layers containing atoms; 4th is minimum vacuum size (both in angstrom)
        #P1 = Poscar(slabgen.get_slab(0))
        #slab = slabgen.get_slab()
        #slabs = slab.get_slabs()
        #req_slab = slabs[0].get_orthogonal_c_slab()

        #slab = slabgen.get_slab(1)
        #req_slab = slab.get_sorted_structure()
        #req_slab = slab.get_orthogonal_c_slab().get_sorted_structure()
        #req_slab.get_sorted_structure().to("poscar",filename="POSCAR")

        #slab2=slabs[0]
        ##slab1=slab.get_slab()
        ##slab2=slab1.get_sorted_structure()
        slab1 = slab.get_slabs()
        slab2 = slab1[0].get_orthogonal_c_slab()
        #slab2.to("poscar",filename="POSCAR.3")
        slab3=slab2
        #slab3=slab2.get_orthogonal_c_slab()

        ### Making POSCAR of unit cell #
        P1=Poscar(slab3)
        #P1 = Poscar(req_slab)
        P2 = P1.get_string(direct=False)
        file_o = open('POSCAR_unit_cell','w+')
        file_o.write(P2)
        file_o.close()

        ### Make Supercell of above ##

        super_slab = Structure.from_file("POSCAR_unit_cell")
        super_slab.make_supercell(slab_dimension)
        super_pos = Poscar(super_slab)
        super_str = super_pos.get_string(direct=False)
        file_o = open('poscar_slab.txt','w+')
        file_o.write(super_str)
        file_o.close()

    @staticmethod
    def get_water_structure(first_param: float, second_param: float, number_of_waters: int) -> str:
        """
        Parameterize water structure
        @params first_param
        @params second_param
        @params number_of_waters
        @returns Multiline string for structure
        """

        return Generator.multiline_strip(
        f"""structure water.pdb
              number {number_of_waters}
              atoms 1 2
                below plane -1.0000   0.0000   0.0000   0.0000
              end atoms
              atoms 1 2
                below plane  0.0000  -1.0000   0.0000   0.0000
              end atoms
              atoms 1 2
                below plane  0.0000    0.0000  -1.0000  -10
              end atoms
              atoms 1 2
                below plane  1.0000    0.0000   0.0000  {first_param}
              end atoms
              atoms 1 2
                below plane  0.0000    1.0000   0.0000  {second_param}
              end atoms
              atoms 1 2
                below plane  0.0000    0.0000   1.0000  50
              end atoms
            end structure""")

    @staticmethod
    def get_yyyy_structure(filename: str, first_param: float, second_param: float, h_min: float, number_of_molecules: int) -> str:
        """
        Parameterize yyyy structure
        @params filename
        @params first_param
        @params second_param
        @params h_min
        @params number_of_molecules
        @returns Multiline string for structure
        """

        return Generator.multiline_strip(
        f"""structure {filename}.pdb
              number {number_of_molecules}
              atoms 23
                inside box 0 0 {h_min} {first_param} {second_param} 50
              end atoms
              atoms 25
                inside box 0 0 {h_min} {first_param} {second_param} 50
              end atoms
            end structure""")

    @staticmethod
    def get_sodium_structure(first_param: float, second_param: float, number_of_ions: int) -> str:
        """
        Parameterize sodium structure
        @params first_param
        @params second_param
        @params number_of_ions
        @returns Multiline string for structure
        """

        return Generator.multiline_strip(
        f"""structure sodium.pdb
              number {number_of_ions}
              atoms 1 2
                below plane -1.0000  0.0000  0.0000  0.0000
              end atoms
              atoms 1 2
                below plane  0.0000 -1.0000  0.0000  0.0000
              end atoms
              atoms 1 2
                below plane  0.0000  0.0000 -1.0000  -10.0000
              end atoms
              atoms 1 2
                below plane  1.0000  0.0000  0.0000  {first_param}
              end atoms
              atoms 1 2
                below plane  0.0000  1.0000  0.0000  {second_param}
              end atoms
              atoms 1 2
                below plane  0.0000  0.0000  1.0000  50
              end atoms
            end structure""")

    @staticmethod
    def get_chlorine_structure(first_param: float, second_param: float, number_of_ions: int) -> str:
        """
        Parameterize chlorine structure
        @params first_param
        @params second_param
        @params number_of_ions
        @returns Multiline string for structure
        """

        return Generator.multiline_strip(
        f"""structure chlorine.pdb
              number {number_of_ions}
              atoms 1 2
                below plane -1.0000  0.0000  0.0000  0.0000
              end atoms
              atoms 1 2
                below plane  0.0000 -1.0000  0.0000  0.0000
              end atoms
              atoms 1 2
                below plane  0.0000  0.0000 -1.0000  -10.0000
              end atoms
              atoms 1 2
                below plane  1.0000  0.0000  0.0000  {first_param}
              end atoms
              atoms 1 2
                below plane  0.0000  1.0000  0.0000  {second_param}
              end atoms
              atoms 1 2
                below plane  0.0000  0.0000  1.0000  50
              end atoms
            end structure""")

    @staticmethod
    def make_yyyy_slab_inp(filename: str, first_param: float, second_param: float, h_min: float, number_of_waters: int, number_of_molecules: int) -> None:
        """
        Parameterize and write yyyy_slab.inp
        @params filename
        @params first_param
        @params second_param
        @params h_min
        @params number_of_waters
        @params number_of_molecules
        @returns None
        """

        s = Generator.multiline_strip(
        f"""seed -1
            tolerance 2.2
            output {filename}_slab.pdb
            filetype pdb
            {Generator.get_water_structure(first_param, second_param, number_of_waters)}
            {Generator.get_yyyy_structure(filename, first_param, second_param, h_min, number_of_molecules)}""")

        Generator.write(f"{filename}_slab.inp", s)

    @staticmethod
    def make_yyyy_slab_ion_inp(filename: str, first_param: float, second_param: float, h_min: float, number_of_waters: int, number_of_molecules: int, number_of_ions: int) -> None:
        """
        Parameterize and write yyyy_slab_ion.inp
        @params filename
        @params first_param
        @params second_param
        @params h_min
        @params number_of_waters
        @params number_of_molecules
        @params number_of_ions
        @returns None
        """

        s = Generator.multiline_strip(
        f"""seed -1
            tolerance 2.2
            output {filename}_slab_ion.pdb
            filetype pdb
            {Generator.get_water_structure(first_param, second_param, number_of_waters)}
            {Generator.get_sodium_structure(first_param, second_param, number_of_ions) if number_of_ions > 0 else ''}
            {Generator.get_chlorine_structure(first_param, second_param, number_of_ions) if number_of_ions > 0 else ''}
            {Generator.get_yyyy_structure(filename, first_param, second_param, h_min, number_of_molecules)}""")

        Generator.write(f"{filename}_slab_ion.inp", s)

    @staticmethod
    def make_output(atoms: List[Atom]) -> None:
        """
        Generate an output file
        @param atoms list of atoms
        @returns None
        """

        index_of_waters = [i for i, atom in enumerate(atoms) if "water" in Atom.get_name(atom.type)]
        x1 = index_of_waters[0] + 1
        x2 = index_of_waters[-1] + 1

        index_of_ions = [i for i, atom in enumerate(atoms) if "ion" in Atom.get_name(atom.type)]
        y1 = index_of_ions[0] + 1
        y2 = index_of_ions[-1] + 1
        
        index_of_molecules = [i for i, atom in enumerate(atoms) if "pfoa" in Atom.get_name(atom.type)]
        z1 = index_of_molecules[0] + 1
        z2 = index_of_molecules[-1] + 1

        s = Generator.multiline_strip(
        f"""first index of waters = {x1}
            last index of waters = {x2}
            first index of ions = {y1}
            last index of ions = {y2}
            first index of molecules = {z1}
            last index of molecules = {z2}""")

        Generator.write(f"output.txt", s)
