#! /usr/bin/python3

import requests
import time
import random

urls = ["https://phack.fr/",
        "https://facebook.com",
        "https://google.com",
        "https://amazon.com",
        "https://youporn.com",
        "https://yahoo.fr",
        "https://youtube.com",
        "https://kiramenekoi.fr",
        "https://laposte.net",
        "https://www.comptia.org/",
        "https://lehack.org/fr",
        "https://www.hackthebox.eu/",
        "https://hackerone.com/",
        "https://www.rapid-flyer.com/",
        "https://www.ineat-group.com/",
        "https://www.intigriti.com/",
        "https://www.yeswehack.com/",
        "https://twitter.com/PhackCTF",
        "https://doodle.com/",
        "https://estcequecestbientotleweekend.fr/",
        "https://github.com/",
        "https://crackstation.net/",
        "http://khtsfdlxrcnmbvzw.neverssl.com/",
        "https://gtfobins.github.io/",
        "https://fr.wikipedia.org/"
    ]

index = 0
for url in urls:

    index += 1
    print(str(index) + "/" + str(len(urls)) + " -- " + url)

    try:
        requests.get(url)
    except:
        pass
    time.sleep(random.randint(2, 3))
    
