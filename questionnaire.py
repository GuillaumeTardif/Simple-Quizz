# PROJET QUESTIONNAIRE

import json

# Made with Python 3.11.0b4


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
        print("***Lancement du questionnaire***")
        print()
        print(f"Catégorie : {self.category}")
        print(f"Titre : {self.quizz_title}")
        print(f"Difficulté : {self.difficulty}")
        print(f"Nombre de question : {len(self.questions)}")
        print()
        current_question_index = 1
        for question in self.questions:
            print(f"QUESTION {current_question_index} sur {len(self.questions)}")
            current_question_index += 1
            if question.poser():
                score += 1
        print("Score final :", score, "sur", len(self.questions))
        return score


# Main Program

questionnaire_list = (
                        ("Les chats", "animaux_leschats"),
                        ("Arts : Musée du louvre", "arts_museedulouvre"),
                        ("Cinéma : Alien", "cinema_alien"),
                        ("Cinéma : Star Wars", "cinema_starwars")
                     )
difficulty_settings = ("debutant",
                       "confirme",
                       "expert",
                      )

# Ask for quizz and difficulty
print("*****JEU DU QUESTIONNAIRE*****")
print("Choisissez un questionnaire:")
for i in range(len(questionnaire_list)):
    print(f' {i+1} - {questionnaire_list[i][0]}')
questionnaire = input(f'Entrez le numéro du questionnaire (entre 1 et {len(questionnaire_list)}) : ')
print()
difficulty = input('Choisissez la difficulté:\n 1 - Débutant\n 2 - Confirmé\n 3 - Expert\n Entrez le numéro de la difficulté (1 à 3) : ')

questionnaire = int(questionnaire)-1
difficulty = int(difficulty)-1

questionnaire_filename = (questionnaire_list[questionnaire][1] + "_" + difficulty_settings[difficulty] + ".json")

# Quizz start
print()
Questionnaire(questionnaire_filename).lancer()

