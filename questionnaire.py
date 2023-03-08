# PROJET QUESTIONNAIRE V3 : POO
#
# - Pratiquer sur la POO
# - Travailler sur du code existant
# - Mener un raisonnement
#
# -> Définir les entitées (données, actions)
#
# Question
#    - titre       - str
#    - choix       - (str)
#    - bonne_reponse   - str
#
#    - poser()  -> bool
#
# Questionnaire
#    - questions      - (Question)
#
#    - lancer()
#
import json


class Question:
    def __init__(self, titre, choix, bonne_reponse):
        self.titre = titre
        self.choix = choix
        self.bonne_reponse = bonne_reponse

    def FromData(data):
        # ....
        q = Question(data[2], data[0], data[1])
        return q

    def poser(self):
        # print("QUESTION")
        print("  " + self.titre)
        for i in range(len(self.choix)):
            print("  ", i + 1, "-", self.choix[i])

        print()
        resultat_response_correcte = False
        reponse_int = Question.demander_reponse_numerique_utlisateur(1, len(self.choix))
        if self.choix[reponse_int - 1].lower() == self.bonne_reponse.lower():
            print("Bonne réponse")
            resultat_response_correcte = True
        else:
            print("Mauvaise réponse")

        print()
        return resultat_response_correcte

    def demander_reponse_numerique_utlisateur(min, max):
        reponse_str = input("Votre réponse (entre " + str(min) + " et " + str(max) + ") :")
        try:
            reponse_int = int(reponse_str)
            if min <= reponse_int <= max:
                return reponse_int

            print("ERREUR : Vous devez rentrer un nombre entre", min, "et", max)
        except:
            print("ERREUR : Veuillez rentrer uniquement des chiffres")
        return Question.demander_reponse_numerique_utlisateur(min, max)


class Questionnaire:
    def __init__(self, filename):
        self.good_answer = None
        self.answer_list = None
        self.question_title = None
        self.filename = filename
        self.questions = []

        file = open(self.filename, "r")
        data = file.read()
        self.json_data = json.loads(data)

        self.category = self.json_data["categorie"]
        self.quizz_title = self.json_data["titre"]
        self.difficulty = self.json_data["difficulte"]

        for question in self.json_data["questions"]:
            self.GetQuestionFromData(question)
            self.questions.append(Question(self.question_title, self.answer_list, self.good_answer))

    def GetQuestionFromData(self, question):
        question_title = question["titre"]
        questions_answer_data = question["choix"]
        answer_list = []
        good_answer = None
        for answer_pair in questions_answer_data:
            answer_list.append(answer_pair[0])
            if answer_pair[1]:
                good_answer = answer_pair[0]

        self.question_title = question_title
        self.answer_list = answer_list
        self.good_answer = good_answer


    def lancer(self):
        score = 0
        print(f"Catégorie : {self.category}")
        print(f"Titre : {self.quizz_title}")
        print(f"Difficulté : {self.difficulty}")
        print(f"Nombre de question : {len(self.questions)}")
        current_question_index = 1
        for question in self.questions:
            print(f"QUESTION {current_question_index} sur {len(self.questions)}")
            current_question_index += 1
            if question.poser():
                score += 1
        print("Score final :", score, "sur", len(self.questions))
        return score


"""questionnaire = (
    ("Quelle est la capitale de la France ?", ("Marseille", "Nice", "Paris", "Nantes", "Lille"), "Paris"), 
    ("Quelle est la capitale de l'Italie ?", ("Rome", "Venise", "Pise", "Florence"), "Rome"),
    ("Quelle est la capitale de la Belgique ?", ("Anvers", "Bruxelles", "Bruges", "Liège"), "Bruxelles")
                )

lancer_questionnaire(questionnaire)"""

# q1 = Question("Quelle est la capitale de la France ?", ("Marseille", "Nice", "Paris", "Nantes", "Lille"), "Paris")
# q1.poser()

# data = (("Marseille", "Nice", "Paris", "Nantes", "Lille"), "Paris", "Quelle est la capitale de la France ?")
# q = Question.FromData(data)
# print(q.__dict__)


Questionnaire(
    "animaux_leschats_debutant.json"
).lancer()
