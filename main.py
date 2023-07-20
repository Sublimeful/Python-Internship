from typing import List, Tuple, Dict
from Generator import *
from Converter import *
from Parser import *
from Atom import *

import os

if __name__ == "__main__":

    # Get user input for filename
    ##filename: str = input("Filename for input file: ")
    filename = 'pfoah'
    ##filename = 'pfoa'

    # Get z-max from user
    ##z_max: float = float(input("z-max: "))
    z_max =  9.23

    # Get .cif file from user
    ##cif_filename: str = input("Filename for .cif file: ")
    cif_filename = 'SiO2.cif'

    # Get slab_dimension
    ##slab_dimension: List[int, ...] = [int(x) for x in input("Enter the slab dimensions (ex: 1 2 3 = 1x2x3): ").split(" ")]
    slab_dimension = [4,4,1]

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
    os.system(f"../packmol/src/packmol < ./{filename}_slab.inp")
    # os.system(f"../../packmol/src/packmol < ./{filename}_slab.inp")
    
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
   
