#!/usr/bin/env python3

from pyexcel_ods import get_data

data = get_data("data/secret.ods")

import json

sheet = json.dumps(data)
print(sheet)

matrix = [["S", "K", "X", "J", "Z", "{", "P"], ["W", "D", "T", "E", "U", "_", "A"], ["C", "L", "B", "G", "F", "V", "O"], ["H", "R", "Y", "N", "I", "M", "Q"], ["}"]]


secret = 'PHACK{_ALLUMER_LE_FEU_ALLUMER_LE_FEU_ET_FAIRE_DANSER_LES_DIABLES_ET_LES_DIEUX_ALLUMER_LE_FEU_ALLUMER_LE_FEU_ET_VOIR_GRANDIR_LA_FLAMME_DANS_VOS_YEUX_ALLUMER_LE_FEU_}'

key_dict = {0: "A", 1: "B", 2: "C", 3: "D", 4: "E", 5: "F", 6: "G"}

for s in secret:
    for r,row in enumerate(matrix):
        for c,col in enumerate(row):
            if s == col:
                note = key_dict[c]
                if r == 0:
                    note += ','
                elif r == 2:
                    note = note.lower()
                elif r == 3:
                    note = note.lower() + "'"
                elif r == 4:
                    note = note.lower() + "''"
                elif r == 5:
                    note = note.lower() + "'''"

                print(note)