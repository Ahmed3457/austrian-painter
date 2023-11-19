from random import shuffle, choice
cubes = {
        "222": [
            "R", "R'", "R2",
            "L", "L'", "L2",
            "U", "U'", "U2",
            "D", "D'", "D2",
            "F", "F'", "F2",
            "B", "B'", "B2"
        ],
        "333": [
            "R", "R'", "R2",
            "L", "L'", "L2",
            "U", "U'", "U2",
            "D", "D'", "D2",
            "F", "F'", "F2",
            "B", "B'", "B2"
        ],
        "444": [
            "R", "R'", "R2", "Rw", "Rw'", "Rw2",
            "L", "L'", "L2", "Lw", "Lw'", "Lw2",
            "U", "U'", "U2", "Uw", "Uw'", "Uw2",
            "D", "D'", "D2", "Dw", "Dw'", "Dw2",
            "F", "F'", "F2", "Fw", "Fw'", "Fw2",
            "B", "B'", "B2", "Bw", "Bw'", "Bw2"
        ],
        "555": [
            "R", "R'", "R2", "Rw", "Rw'", "Rw2",
            "L", "L'", "L2", "Lw", "Lw'", "Lw2",
            "U", "U'", "U2", "Uw", "Uw'", "Uw2",
            "D", "D'", "D2", "Dw", "Dw'", "Dw2",
            "F", "F'", "F2", "Fw", "Fw'", "Fw2",
            "B", "B'", "B2", "Bw", "Bw'", "Bw2"
        ],
        "666": [
            "R", "R'", "R2", "Rw", "Rw'", "Rw2",
            "L", "L'", "L2", "Lw", "Lw'", "Lw2",
            "U", "U'", "U2", "Uw", "Uw'", "Uw2",
            "D", "D'", "D2", "Dw", "Dw'", "Dw2",
            "F", "F'", "F2", "Fw", "Fw'", "Fw2",
            "B", "B'", "B2", "Bw", "Bw'", "Bw2"
        ],
        "777": [
            "R", "R'", "R2", "Rw", "Rw'", "Rw2",
            "L", "L'", "L2", "Lw", "Lw'", "Lw2",
            "U", "U'", "U2", "Uw", "Uw'", "Uw2",
            "D", "D'", "D2", "Dw", "Dw'", "Dw2",
            "F", "F'", "F2", "Fw", "Fw'", "Fw2",
            "B", "B'", "B2", "Bw", "Bw'", "Bw2"
        ]
}
def gen_scramble(length=20, cube="333"):
    scramble=""
    for i in range(length):
        shuffle(cubes[cube])
        x = choice(cubes[cube])
        scramble += x + " "
    return scramble