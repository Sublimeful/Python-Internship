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

    # Get user input for filename
    filename = input_params["filename"]

    # Get z-max from user
    z_max = literal_eval(input_params["z_max"])

    # Get .cif file from user
    cif_filename = input_params["cif_filename"]

    # Get slab_dimension
    slab_dimension = literal_eval(input_params["slab_dimension"])

    # Get packmol file path
    packmol_location = input_params["packmol_location"]

    # Generate poscar_slab using cif file and slab_dimension
    Generator.make_slab(cif_filename=cif_filename, slab_dimension=slab_dimension)
    
    # Read poscar_slab.txt
    Parser.read_file("poscar_slab.txt")

    # Get first param
    first_param = float([part.strip() for part in Parser.get_line(2).split(" ") if part != ""][0])

    # Get second param
    second_param = float([part.strip() for part in Parser.get_line(3).split(" ") if part != ""][1])

    # Generate yyyy_slab.inp with params
    Generator.make_yyyy_slab_inp(filename, first_param, second_param)

    # Run packmol using X_slab.inp and X.pdb
    os.system(f"{packmol_location} < ./{filename}_slab.inp")
    
    # Convert packmol output file to new input(output.txt)
    # 1. Parse packmol output to list of atoms
    Parser.read_file(f"./{filename}_slab.pdb")
    Parser.parse()
    atoms: List[Atom] = Parser.extract()

    # 2. Convert list of atoms to list of lines representing output
    Converter.analyze(atoms)
    Converter.generate(header="# water and pfoah on sio2 slab")
    output_lines: List[str] = Converter.extract()

    # Write output to file (data_X_water.txt)
    Generator.write_lines(filepath=f"data_{filename}_water.txt", lines=output_lines)

    # 1. Parse poscar_slab.txt
    Parser.read_file("./poscar_slab.txt")
    Parser.parse_poscar()
    atoms: List[Atom] = Parser.extract()

    # Set options
    Converter.options = Converter.Options(z_max = z_max)

    # 2. Convert to output
    Converter.analyze(atoms)
    Converter.generate(header="# sio2 slab  100 facet  4x4x1 supercell made from premitive cell, mp-??????")
    output_lines: List[str] = Converter.extract()

    # Write output to file (data_X_water.txt)
    Generator.write_lines(filepath=f"data_slab.txt", lines=output_lines)
   
