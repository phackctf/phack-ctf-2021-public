#! /usr/bin/env python3

import random
import os

FLAG = "PHACK{R3ady_4_a_z1pl1n3_r1d3}"
file = "nothing.here"
count = 0
archives_names = ["junky", "data", "stuff", "nothing", "flag"]

def round(name):
    global count, file

    if count%3 == 0:
        archive_name =  name + ".zip"

        if count == 333 or count == 513 or count == 822 or count == 1014:
            os.system("zip -e {} {}".format(archive_name, file))
        else:
            os.system("zip {} {} > /dev/null".format(archive_name, file))

    elif count%3 == 1:
        archive_name =  name + ".tar.gz"
        os.system("tar -cvzf {} {} > /dev/null".format(archive_name, file))

    else:
        archive_name =  name + ".rar"
        os.system("rar a {} {} > /dev/null".format(archive_name, file))

    if "nothing.here" != file:
        os.system("rm {}".format(file))

    print(archive_name + " archive created!")
    file = archive_name
    count += 1

for c in FLAG[::-1]:
    round(c)

for index in range(1024 - 1  - len(FLAG)):
    round(random.choice(archives_names))

os.system("zip {} {} {}".format("challenge2.zip", file, "password.lst"))
os.system("rm {}".format(file))
