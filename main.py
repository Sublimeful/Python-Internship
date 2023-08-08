# how to run this code:
# python3.7 main.py < input.txt
#
import os
from ast import literal_eval
from typing import List, Tuple, Dict
from Generator import *
from Converter import *
from Parser import *
from Atom import *

if __name__ == "__main__":
    # Read input file and extract input params
    input_params = Parser.read_input_file("input.txt")
    z_max: float = float(eval(input_params["z_max"]))
    h_min: float = float(eval(input_params["h_min"]))
    number_of_ions: int = int(eval(input_params["number_of_ions"]))
    number_of_waters: int = int(eval(input_params["number_of_waters"]))
    number_of_molecules: int = int(eval(input_params["number_of_molecules"]))
    slab_dimension: List = eval(input_params["slab_dimension"])
    filename: str = input_params["filename"]
    cif_filename: str = input_params["cif_filename"]
    packmol_location: str = input_params["packmol_location"]

    # Generate poscar_slab using cif file and slab_dimension
    Generator.make_slab(cif_filename=cif_filename, slab_dimension=slab_dimension)
    
    # Read poscar_slab.txt
    Parser.read_file("poscar_slab.txt")

    # Get first and second params
    first_param = float([part.strip() for part in Parser.get_line(2).split(" ") if part != ""][0])
    second_param = float([part.strip() for part in Parser.get_line(3).split(" ") if part != ""][1])

    # Generate input file(s) with params
    Generator.make_yyyy_slab_ion_inp(filename, first_param, second_param, h_min, number_of_waters, number_of_molecules, number_of_ions)

    # Run packmol on input file(s)
    os.system(f"{packmol_location} < ./{filename}_slab_ion.inp")
    
    # Parse output file to list of atoms
    Parser.read_file(f"./{filename}_slab_ion.pdb")
    Parser.parse()
    atoms: List[Atom] = Parser.extract()

    # Convert list of atoms to list of lines representing output
    Converter.analyze(atoms)
    Converter.generate(header=f"# water and {filename} on sio2 slab")
    output_lines: List[str] = Converter.extract()

    # Write output to file
    Generator.write_lines(filepath=f"data_{filename}_water{'_ion' if number_of_ions > 0 else ''}.txt", lines=output_lines)

    # Parse poscar_slab.txt
    Parser.read_file("./poscar_slab.txt")
    Parser.parse_poscar()
    atoms: List[Atom] = Parser.extract()

    # Convert to output
    Converter.options = Converter.Options(z_max = z_max)
    Converter.analyze(atoms)
    Converter.generate(header="# sio2 slab  100 facet  4x4x1 supercell made from premitive cell, mp-??????")
    output_lines: List[str] = Converter.extract()

    # Write output to file
    Generator.write_lines(filepath=f"data_slab.txt", lines=output_lines)



