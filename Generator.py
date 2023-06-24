from typing import List, Tuple, Dict

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
    Generates an input(inp) file for packmol
    """
    @staticmethod
    def generate_input(filename: str):
        lines = []
        lines.append("seed -1")
        lines.append("tolerance 2.0")
        lines.append(f"output {filename}_slab.pdb")
        lines.append("filetype pdb")
        lines.append("structure water.pdb")
        lines.append("  number 67")
        lines.append("  atoms 1 2 3")
        lines.append("    over plane 0.0000  0.0000   1.0000   11.5")
        lines.append("  end atoms")
        lines.append("  atoms 1 2 3")
        lines.append("    below plane 0.0000  0.0000   1.0000  31.5000")
        lines.append("  end atoms")
        lines.append("  atoms 1 2 3")
        lines.append("    below plane 0.0000  -1.0000   0.0000   0.0000")
        lines.append("  end atoms")
        lines.append("  atoms 1 2 3")
        lines.append("    over plane 0.0000  -1.0000   0.0000 -12.9327")
        lines.append("  end atoms")
        lines.append("  atoms 1 2 3")
        lines.append("    over plane 0.9001  -0.4356  -0.0000   0.0000")
        lines.append("  end atoms")
        lines.append("  atoms 1 2 3")
        lines.append("    below plane 0.9001 -0.4356  0.0000 12.5248")
        lines.append("  end atoms")
        lines.append("end structure")
        lines.append("")
        lines.append("structure hydroxyl.pdb")
        lines.append("  number 74")
        lines.append("  atoms 1 2")
        lines.append("    over plane 0.0000  0.0000   1.0000   11.5")
        lines.append("  end atoms")
        lines.append("  atoms 1 2")
        lines.append("    below plane 0.0000  0.0000   1.0000  31.5000")
        lines.append("  end atoms")
        lines.append("  atoms 1 2")
        lines.append("    below plane 0.0000  -1.0000   0.0000   0.0000")
        lines.append("  end atoms")
        lines.append("  atoms 1 2")
        lines.append("    over plane 0.0000  -1.0000   0.0000 -12.9327")
        lines.append("  end atoms")
        lines.append("  atoms 1 2")
        lines.append("    over plane 0.9001  -0.4356  -0.0000   0.0000")
        lines.append("  end atoms")
        lines.append("  atoms 1 2")
        lines.append("    below plane 0.9001 -0.4356  0.0000 12.5248")
        lines.append("  end atoms")
        lines.append("end structure")
        lines.append("")
        lines.append(f"structure {filename}.pdb")
        lines.append("  inside cube 0. 0. 0. 100.")
        lines.append("  atoms 12")
        lines.append("    inside box 8.5 5.5 17 9.5 6.5 18")
        lines.append("  end atoms")
        lines.append("  atoms 1")
        lines.append("    inside box 0 0 11 20 20 12")
        lines.append("  end atoms")
        lines.append("end structure")
        return lines
