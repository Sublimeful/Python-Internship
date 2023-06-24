from typing import List, Tuple, Dict
from Generator import *
from Converter import *
from Parser import *
from Atom import *

import os

if __name__ == "__main__":

    # Get user input for filename
    filename: str = input("Filename: ")

    # Generate packmol input file
    input_lines: List[str] = Generator.generate_input(filename)
    # Write input file to X_slab.inp
    Generator.write_lines(filepath=f"{filename}_slab.inp", lines=input_lines)
    # Run packmol
    os.system(f"../packmol/src/packmol < ./{filename}_slab.inp")

    # Convert packmol output file to new input(output.txt)
    # 1. Parse packmol output to list of atoms
    Parser.read_file(f"./{filename}_slab.pdb")
    Parser.parse()
    atoms: List[Atom] = Parser.extract()

    # 2. Convert list of atoms to list of lines representing output
    Converter.analyze(atoms)
    Converter.generate()
    output_lines: List[str] = Converter.extract()

    # Write output to file (data_X_water_random.txt)
    Generator.write_lines(filepath=f"data_{filename}_water_random.txt", lines=output_lines)
    # Generator.write_lines(filepath=f"data_{filename}_water.txt", lines=output_lines)
