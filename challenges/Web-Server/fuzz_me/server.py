#!usr/bin/python3

from flask import Flask, render_template, send_from_directory, request, Response, jsonify
import signal
import sys
import os

HOST = ''
PORT = 80

SESSIONS = ["eyJ1c2VyIjogIjY1YTlmYzRjLWIwNDYtNDE3OS1iMDE5LTdlMDcxZDFjZTc5ZiIsICJpc0FkbWluIiA6IGZhbHNlLCAid2VpcmRfc3R1ZmYiIDogIitBSEc5NUZKeHRzNGoxNFJuTHdxaEE9PSIsICJoYXBweV9zbWlsZXkiIDogIvCfmI0ifQ==",
            "eyJ1c2VyIjogIjkwNjhjY2ZmLTBkOTgtNGViNS1iMjdkLTQyZDcwZTQyYmRkZCIsICJpc0FkbWluIiA6IGZhbHNlLCAid2VpcmRfc3R1ZmYiIDogIkkvS3M1clg0SGJSb2hhbm9pc1lUOXc9PSIsICJoYXBweV9zbWlsZXkiIDogIvCfpoQifQ==",
            "eyJ1c2VyIjogImIwZWU5YjNjLTdkNjMtNDQwZi05ZDcyLWM3NTg2ODZiMDVlNCIsICJpc0FkbWluIiA6IGZhbHNlLCAid2VpcmRfc3R1ZmYiIDogIjYwY3k4bUJrM3luOFNhRisvSGVhUHc9PSIsICJoYXBweV9zbWlsZXkiIDogIvCfkp0ifQ==",
            "eyJ1c2VyIjogIjEzYTE0NTExLTc3NzktNDJmNS04MjliLTc1OTc3MzRjODc0YyIsICJpc0FkbWluIiA6IGZhbHNlLCAid2VpcmRfc3R1ZmYiIDogIjRVQWljczZ3TzkvVzM3Qjd2Q0NQT3c9PSIsICJoYXBweV9zbWlsZXkiIDogIvCfmYsifQ==",
            "eyJ1c2VyIjogIjg3MmUwYTQxLTk5ZTUtNGU3Ni1hNWU3LTk2MDkzNzU3ZmE4MSIsICJpc0FkbWluIiA6IHRydWUsICJ3ZWlyZF9zdHVmZiIgOiAiU1NCaGJTQjBhR1VnWVdSdGFXNGdJUT09IiwgImhhcHB5X3NtaWxleSIgOiAi8J+RqOKAjfCfjbMifQ==",
            "eyJ1c2VyIjogIjk2OGYyZTlkLTI3YzEtNDUwMy05NzM5LTNiMWM4NjMwNjU2NCIsICJpc0FkbWluIiA6IGZhbHNlLCAid2VpcmRfc3R1ZmYiIDogIllOK1pWNWxTMkZTNjlaMmhmd1RaT3c9PSIsICJoYXBweV9zbWlsZXkiIDogIvCfjIgifQ==",
            "eyJ1c2VyIjogIjViNTgwMDcyLTM2YzAtNDU0Yi04NThiLTVmZmJjOTRiNjgyNSIsICJpc0FkbWluIiA6IGZhbHNlLCAid2VpcmRfc3R1ZmYiIDogIkZkNWlPVU9qMDJrZmU0aDMyOGplNHc9PSIsICJoYXBweV9zbWlsZXkiIDogIvCfkoMifQ=="]

UUID = "872e0a41-99e5-4e76-a5e7-96093757fa81"
LOGIN = "admin"
PASSWORD = "NeOIsTh3T4rget<3"
FLAG = "PHACK{th1s_1s_H0w_w3_d0_enum3r4ti0n_m4n}"

app = Flask(__name__)


def keyboardInterruptHandler(signal, frame):
    sys.exit(0)


@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")


@app.route('/css/<page>', methods=['GET'])
def css(page):
        return send_from_directory(os.path.join(app.root_path, 'static', 'css'), page)


@app.route('/fonts/<page>', methods=['GET'])
def fonts(page):
        return send_from_directory(os.path.join(app.root_path, 'static', 'fonts'), page)


@app.route('/images/<page>', methods=['GET'])
def images(page):
        return send_from_directory(os.path.join(app.root_path, 'static', 'images'), page)


@app.route('/js/<page>', methods=['GET'])
def js(page):
        return send_from_directory(os.path.join(app.root_path, 'static', 'js'), page)


@app.route('/api/sessions', methods=['GET'])
def sessions():
    return jsonify({"sessions": SESSIONS})


@app.route('/api/user', methods=['GET'])
def user():
    if "uuid" not in request.args:
        response = Response('{"error": "Paramètre manquant !"}', 400)
        response.mimetype = "application/json"
        return response
    elif request.args.get('uuid') == UUID:
        response = Response('{"info": {"name" : "Biden", "firstname" : "Joe", "login" : "' + LOGIN + '", "password" : "' + PASSWORD + '", "description":"Président, tout simplement."}}', 200)
        response.mimetype = "application/json"
        return response
    else:
        response = Response('{"error": "Uuid inconnu !"}', 500)
        response.mimetype = "application/json"
        return response


@app.route('/api/login', methods=['POST'])
def login():
    login = request.form.get('user')
    passwd = request.form.get('pass')

    if login == LOGIN and passwd == PASSWORD:
        return jsonify({"success": True, "redirect": "/voici-le-flag-il-suffisait-de-demander"})
    else:
        return jsonify({"success": False, "msg": "Mauvais login et/ou mot de passe"})


@app.route('/voici-le-flag-il-suffisait-de-demander', methods=['GET'])
def flag():
    text = """
          _ |                           _____________________________
-'||````------.....___          |     ,;;;;;;  ,;;,`WW,   MW|
  ||     _ _          |         |    ;;;;';;' ';';; `WMn  WM|
  ||    (`\-\         |         |    ';;  _   _      `MWn,MW|
  ||    '  (ee        |         |        ( `-('\      `MMWbM|
  ||    ; ' / *   .,, |         |        'a.a ` \      `lWMb|
  ||   /.\_ .-'  '''/ |         |        (" \' )/        `WM|
  ||  '  `._(  .' ,.' |         |=======_.`- / /;-,_========|
  ||  l     \-'   /   |         |     ,' / `._.' `; `,    Ww|
  ||  |   ; r\  ,'    |         |    '   ; ,  ,o  /   `   MM|
  ||  ;'--; LJ;'      |         |   /   ,; 8o "o8 \.   \  ]W|
  ||  \   \   |   ()` [         |  f   ' /  8 8o' | `   ` MW|
  ||  |\   l=[;       |         |  ;  f  |,_...__ \  Y  ; [M|
  ||  | `_,' '        |         |_ > -; ,'     _.``; > -)_WW|
  ||   \    f|        |         '-<<(('/     ,     ;<(((----'
  ||   |    |;        |               /'`-, ;\     l
  ||   \    l'        |              (    .'  Y'~`-j
  ||   /;   )         |               \   `   (    l
  ||  / \   |         |----------------\   \---;   |---------------------
 .'``/  |   ;-.....___|                 \   \  l   l
'   /_,.|   l                           _>,  ) ;, .;
   (_   l-~'`._                        <(((./  /   ;
     `--`._..,))                               (|li'



        Bravo, voici le flag : """ + FLAG + """



                                  **********
                              **              ***
                          **                      **
                       ***                           **
                     ***                                *
                    **                                    *
                  **                                       **
                 **                                         **
                **       .  ****  **   ***   ***** ******     *
               **     *** **  *** *** ********    ***** .      **
              *      *****    ****** ***.** ********            .*
             **       **                                  **      *
            **    **              **************.       *****      *
           **    *****         ***.    ** ******       *******      *
           **    *******       *****  **   **          *******      **
          **     ********                             ********       *
          **      ********     ,*             ,*****  ********        *
          **      *********  ********      ********** *******         *
          *        ******** ********************************
          *          *************************************            *
          **           ***************************************        *
          **       *************************************             *
           **             ******** *********************             *
            **             *****************************            *
             **            ************** *************           **
              ***            ************************            *
                **                                             *
                  ***                                        *
                     ***                                 ***
                        ****                         ***
                             ****** *        ******

    """

    response = Response(text, 200)
    response.mimetype = "text/plain"
    return response


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
          'favicon.ico',mimetype='image/vnd.microsoft.icon')


def main():
    app.run('0.0.0.0', PORT, False)


if __name__ == "__main__":
    signal.signal(signal.SIGINT, keyboardInterruptHandler)
    main()
