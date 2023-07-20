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
class Generator():
    """
    Writes newline separated strings to filepath
    """
    @staticmethod
    def write_lines(filepath: str, lines: List[str]) -> None:
        with open(filepath, "w+") as file:
            file.write("\n".join(lines))
            file.close()

    """
    Generates poscar_slab.txt from slab_dimension using TiO2_rutile.cif
    """
    @staticmethod
    def make_slab(cif_filename: str, slab_dimension: List) -> None:
    ##def make_slab(cif_filename: str, slab_dimension: List[int, ...]) -> None:
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

    """
    Parameterize yyyy_slab.inp
    """
    def make_yyyy_slab_inp(filename: str, first_param: float, second_param: float) -> None:
        res = f"""
            tolerance 2.0
            output pfoah_slab.pdb
            filetype pdb
            structure water.pdb
              number 572
              atoms 1 2
                below plane -1.0000   0.0000   0.0000   0.0000
              end atoms
              atoms 1 2
                below plane  0.0000  -1.0000   0.0000   0.0000
              end atoms
              atoms 1 2
                below plane  0.0000    0.0000  -1.0000  -10.0000
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
            end structure
            structure pfoah.pdb
              number 10
              atoms 23
                inside box 0 0 15 {first_param} {second_param} 50
              end atoms
              atoms 25
                inside box 0 0 15 {first_param} {second_param} 50
              end atoms
            end structure
        """

        with open(f"{filename}_slab.inp", "w+") as file:
            file.write(res)
            file.close()
