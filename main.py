from typing import List, Tuple, Dict
from Generator import *
from Converter import *
from Parser import *
from Atom import *

import os

if __name__ == "__main__":
    # Generate packmol input file
    input_lines: List[str] = Generator.generate_input()
    # Write input file to pfoa_slab.inp
    Generator.write_lines(filepath="pfoa_slab.inp", lines=input_lines)
    # Run packmol
    os.system("../src/packmol < ./pfoa_slab.inp")

    # Convert packmol output file to new input(output.txt)
    # 1. Parse packmol output to list of atoms
    Parser.read_file("./pfoa_slab.pdb")
    Parser.parse()
    atoms: List[Atom] = Parser.extract()

    # 2. Convert list of atoms to list of lines representing output
    Converter.analyze(atoms)
    Converter.generate()
    output_lines: List[str] = Converter.extract()

    # Write output to file (data_pfoa_water_random.txt)
    Generator.write_lines(filepath="data_pfoa_water_random.txt", lines=output_lines)
