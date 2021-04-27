import random

class User:
    def __init__(self, id):
        self.id = id
        self.step = 0
        self.current_question = 0
        self.questions = self.get_random_questions()
        self.asked_time = None

    def get_random_questions(self):
        questions = list(range(0,len(QUESTIONS)))
        random.shuffle(questions)
        return questions


class Question:
    def __init__(self, index, label, answer):
        self.index = index
        self.label = label
        self.answer = answer


class Step:
    INIT = 0
    WANNA_PLAY = 1
    INSTRUCTION = 2
    PLAYING = 3
    WIN = 4


QUESTIONS = []
USERS = {}
FLAG = "PHACK{i_4m_th3_w1k1_b0t}"
DELAY = 3

QUESTIONS.append(Question(1, "What is the date of birth of Barack Obama❓ (Format: MM/dd/YYYY)", "08/04/1961"))
QUESTIONS.append(Question(2, "What is the full name of birth of Billie Eilish❓", "Billie Eilish Pirate Baird O'Connell"))
QUESTIONS.append(Question(3, "What is the nationality of Gal Gadot❓", "Israeli"))
QUESTIONS.append(Question(4, "How old is Omar Sy❓", "43"))
QUESTIONS.append(Question(5, "What is the birthplace of Daniel Ricciardo❓", "Perth"))
QUESTIONS.append(Question(6, "What is the best CTF event so far❓ (Just answer \"P'HackCTF\")", "P'HackCTF"))
