#!/usr/local/bin/python3

from lxml import etree
from datetime import datetime
import sqlite3
import os, sys

GRADE_FOLDER_PATH = '/home/teacher/evaluations/'
DB_FILENAME = "/home/rector/graduation.db"

class Person:

    def __init__(self, first_name, last_name):
      self.first_name = first_name
      self.last_name = last_name

    def is_validated(self):
        if len(self.first_name) > 15:
            return False
        elif len(self.last_name) > 15:
            return False
        else:
            return True


class Evaluation:

    def __init__(self, grade, subject, comment, student, teacher):
        self.grade = grade
        self.subject = subject
        self.comment = comment
        self.student = student
        self.teacher = teacher

    def is_validated(self):
        if len(self.subject) > 20:
            return False
        elif not self.grade.isnumeric() or int(self.grade) < 0 or int(self.grade) > 20:
            return False
        elif not self.student.is_validated():
            return False
        elif not self.teacher.is_validated():
            return False
        else:
            return True


def init_db():
    if not os.path.isfile(DB_FILENAME):
        cprint("[+] Création de la base de données.");

        conn = sqlite3.connect(DB_FILENAME)
        conn.execute('''CREATE TABLE evaluations
                         (ID INTEGER PRIMARY KEY  AUTOINCREMENT,
                         SUBJECT       TEXT    NOT NULL,
                         GRADE         INT     NOT NULL,
                         COMMENT       TEXT            ,
                         TEACHER       TEXT    NOT NULL,
                         STUDENT       TEXT    NOT NULL);''')
        conn.commit()
        conn.close()


def insert_data_into_database(evaluation):

    evaluation.subject = evaluation.subject.replace("'", "\\'")
    evaluation.comment = evaluation.comment.replace("'", "\\'")
    evaluation.teacher.first_name = evaluation.teacher.first_name.replace("'", "\\'")
    evaluation.teacher.last_name = evaluation.teacher.last_name.replace("'", "\\'")
    evaluation.student.first_name = evaluation.student.first_name.replace("'", "\\'")
    evaluation.student.last_name = evaluation.student.last_name.replace("'", "\\'")

    conn = sqlite3.connect(DB_FILENAME)
    query = "INSERT INTO evaluations (SUBJECT,GRADE,COMMENT,TEACHER,STUDENT) VALUES ('{}', '{}', '{}', '{}', '{}')".format(evaluation.subject, evaluation.grade, evaluation.comment, evaluation.teacher.first_name.capitalize() + " " + evaluation.teacher.last_name.upper(), evaluation.student.first_name.capitalize() + " " + evaluation.student.last_name.upper())

    conn.execute(query);
    conn.commit()
    conn.close()

    cprint("[+] Nouvelle évaluation ajoutée.")


def cprint(text):
    print(datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "\t" + text)


def move_file(filename):
    if not os.path.exists(GRADE_FOLDER_PATH + "done/"):
        os.mkdir(GRADE_FOLDER_PATH + "done/")

    os.rename(GRADE_FOLDER_PATH + filename, GRADE_FOLDER_PATH + "done/" + filename)


def process():
    parser = etree.XMLParser()

    cprint("[+] Analye des fichiers dans \"{}\".".format(GRADE_FOLDER_PATH))
    for filename in os.listdir(GRADE_FOLDER_PATH):
        if filename.endswith(".xml"):
            cprint("[+] Fichier \"{}\" en cours d'analyse.".format(filename))
            f = open(GRADE_FOLDER_PATH + filename)
            content = f.read()

            tree = etree.parse(GRADE_FOLDER_PATH + filename, parser)
            root = tree.getroot()

            for elem in root.iter():
                if elem.tag == "student":
                    student = Person(elem[0].text, elem[1].text)
                elif elem.tag == "teacher":
                    teacher = Person(elem[0].text, elem[1].text)
                elif elem.tag == "grade":
                    grade = elem.text
                elif elem.tag == "subject":
                    subject = elem.text
                elif elem.tag == "comment":
                    comment = elem.text

            evaluation = Evaluation(grade, subject, comment, student, teacher)

            if evaluation.is_validated():
                insert_data_into_database(evaluation)
            else:
                cprint("[-] Données non conformes. Arrêt.")
                sys.exit(1)


            cprint("[+] Fichier \"{}\" analysé.".format(filename))
            move_file(filename)
        elif "done" not in filename:
            cprint("[-] Fichier \"{}\" non accepté.".format(filename))


if __name__ == "__main__":
    cprint("[+] Lancement de l'intégration")
    init_db()
    process()
    cprint("[+] Intégration terminée\n\n")
