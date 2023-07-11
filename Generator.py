# Import pymatgen dependancies
from pymatgen.core.surface import SlabGenerator, Structure, ReconstructionGenerator
from pymatgen.io.vasp.inputs import Poscar

class Generator():
    """
    Writes newline separated strings to filepath
    """
    @staticmethod
    def write_lines(filepath: str, lines: list[str]) -> None:
        with open(filepath, "w+") as file:
            file.write("\n".join(lines))
            file.close()

    """
    Generates poscar_slab.txt from slab_dimension using TiO2_rutile.cif
    """
    @staticmethod
    def make_slab(slab_dimension: list[int, ...]) -> None:
        ### Slab generator code ###
        ### by Srishyam Raghavan (02/17/2020) ###

        structure = Structure.from_file("TiO2_rutile.cif")   # import Structure before= this
        slab = SlabGenerator(structure,(1,1,0),4,25,center_slab=True)  # 2nd is (h,k,l); 3rd is minimum size of layers containing atoms; 4th is minimum vacuum size (both in angstrom)
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
        slab1=slab.get_slab()
        slab2=slab1.get_sorted_structure()
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
