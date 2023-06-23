import os

def generate_input():
    lines = []
    lines.append("seed -1")
    lines.append("tolerance 2.0")
    lines.append("output pfoa_slab.pdb")
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
    lines.append("structure pfoa.pdb")
    lines.append("  inside cube 0. 0. 0. 100.")
    lines.append("  atoms 12")
    lines.append("    inside box 8.5 5.5 17 9.5 6.5 18")
    lines.append("  end atoms")
    lines.append("  atoms 1")
    lines.append("    inside box 0 0 11 20 20 12")
    lines.append("  end atoms")
    lines.append("end structure")

    with open("pfoa_slab.inp", "w+") as file:
        file.write("\n".join(lines))
        file.close()

def run_packmol():
    os.system("../src/packmol < ./pfoa_slab.inp")

if __name__ == "__main__":
    generate_input()
    run_packmol()


