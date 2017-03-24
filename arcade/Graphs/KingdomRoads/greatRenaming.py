def greatRenaming(roadRegister):
    p = []
    row = -1
    for r in roadRegister:
        col = -1
        nRow = []
        for c in r:
            nRow.append(roadRegister[row][col])
            col += 1
        row += 1
        p.append(nRow)
    return p


roadRegister = [[False, True,  True,  False],
                [True,  False, True,  False],
                [True,  True,  False, True ],
                [False, False, True,  False]]

print greatRenaming(roadRegister) == [[False, False, False, True ],
                               [False, False, True,  True ],
                               [False, True,  False, True ],
                               [True,  True,  True,  False]]