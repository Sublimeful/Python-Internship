from Generator import *
from Converter import *
from Parser import *
from Atom import *

import os

if __name__ == "__main__":

    # Get user input for filename
    filename: str = input("Filename: ")

    # Get z-max from user
    z_max: float = float(input("z-max: "))

    # Get slab_dimension
    slab_dimension: list[int, ...] = [int(x) for x in input("Enter the slab dimensions (ex: 1 2 3 = 1x2x3): ").split(" ")]

    # Run packmol using user provided X_slab.inp and X.pdb
    os.system(f"../packmol/src/packmol < ./{filename}_slab.inp")

    # Convert packmol output file to new input(output.txt)
    # 1. Parse packmol output to list of atoms
    Parser.read_file(f"./{filename}_slab.pdb")
    Parser.parse()
    atoms: list[Atom] = Parser.extract()

    # 2. Convert list of atoms to list of lines representing output
    Converter.analyze(atoms)
    Converter.generate(header="# water and pfoah on sio2 slab")
    output_lines: list[str] = Converter.extract()

    # Write output to file (data_X_water.txt)
    Generator.write_lines(filepath=f"data_{filename}_water.txt", lines=output_lines)

    # Generate poscar_slab using slab_dimension
    Generator.make_slab(slab_dimension)

    # 3. Parse poscar_slab.txt
    Parser.read_file("./poscar_slab.txt")
    Parser.parse_poscar()
    atoms: list[Atom] = Parser.extract()

    # Set options
    Converter.options = Converter.Options(z_max = z_max)

    # 4. Convert to output
    Converter.analyze(atoms)
    Converter.generate(header="# sio2 slab  100 facet  4x4x1 supercell made from premitive cell, mp-??????")
    output_lines: list[str] = Converter.extract()

    # Write output to file (data_X_water.txt)
    Generator.write_lines(filepath=f"data_slab.txt", lines=output_lines)



