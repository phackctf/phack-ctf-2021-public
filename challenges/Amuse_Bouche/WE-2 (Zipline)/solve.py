#! /usr/bin/env python3

import os

keep = True
stdout = ""

COMMANDS = """
    mkdir ./out && \
    cp challenge.zip ./out/ && \
    cd ./out && \
    unzip challenge.zip && \
    rm -rf challenge.zip password.lst
"""

os.system(COMMANDS)


while keep:
    try:
        file = os.listdir("./out")[0]
        stdout += file.split(".")[0]

        if ".tar.gz" in file:
            os.system("cd out && tar -xvzf {} > /dev/null".format(file))
        if ".rar" in file:
            os.system("cd out && unrar x {} > /dev/null".format(file))
        if ".zip" in file:
            os.system("cd out && unzip " + file)

        if file != "out":
            os.system("rm ./out/" + file)

    except:
        keep = False

print("FLAG is : " + stdout.replace("data", "").replace("junky", "").replace("stuff", "").replace("nothing", "").replace("flag", "").replace("nothing", ""))

os.system("rm -rf ./out")
