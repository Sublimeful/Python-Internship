### Script to find and add [OH] on adsorption sites from Required Slab ###
### by Srishyam Raghavan (02/19/2020) ###

import sys
sys.path.insert(1, '/usr/local/anaconda3/lib/python3.7/site-packages/')
from pymatgen.core.structure import Molecule as Molec
from pymatgen.core.surface import SlabGenerator, Structure, ReconstructionGenerator
from pymatgen.io.vasp.inputs import Poscar
from pymatgen.analysis.adsorption import AdsorbateSiteFinder as ASF

slab1 = Structure.from_file("/mnt/hdd1/sragha20/Projects/Project_Adsorption_Energy/python_codes/slab_generation/POSCAR")
req_slab = slab1
Po1 = ASF(req_slab, selective_dynamics=True, height=1.0)		# height is in angstrom (below which all atoms will be frozen)
site_list = Po1.find_surface_sites_by_height(req_slab)

species = ['C','O','O']
positions = [[0, 0, 0],[1.16, 0, 0],[-1.16, 0, 0]]
co2 = Molec(species,positions)

structs = Po1.generate_adsorption_structures(co2,min_lw=4.0) 	# Get all possible adsorption structures

# Print each structure into a different POSCAR  #
i = 0
for x in structs:
	i += 1
	P1 = Poscar(x)
	P2 = P1.get_string(direct=False)
	f = open('POSCAR.%i' %i, 'w+')
	f.write(P2)
	f.close()
	

