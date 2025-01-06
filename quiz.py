from time import sleep as wait

class Questions:
    def __init__(self, question: str, correct_response: str):
        self.question = question
        self.correct_response = correct_response.lower()
        self.score = 0

    def ask_question(self):
        print(self.question)
        user_answer: str = input("Resposta: ").strip().lower()
        if user_answer == self.correct_response:
            print("Correto!")
            self.score += 10
            print(f"Score: {self.score}")
        else:
            print("Errado")
            print(f"Score: {self.score}")
    def final(self):
        print("\nAcabou!")
        print(f"Pontuação final: {self.score}")

    def get_score(self):
        return int(self.score)


def start():
    print("QUIZ")
    answer_user: str = input("Quer começar? [S/N] ").strip().lower()
    if answer_user != "s":
        print("Saindo...")
        quit()
    print("Começando...")
    wait(2)
