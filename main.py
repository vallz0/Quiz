import quiz

def main():
   quiz.start()
   question1 = quiz.Questions(
       "Qual é a capital da França??\n"
       "A) Berlim\n"
       "B) Madri\n"
       "C) Paris\n"
       "D) Londres\n",
       "c"
   )
   question1.ask_question()

   question2 = quiz.Questions(
       "Qual é o maior planeta do sistema solar?\n"
       "A) Terra\n"
       "B) Marte\n"
       "C) Júpiter\n"
       "D) Saturno\n",
       "c"
   )
   question2.ask_question()

   question3 = quiz.Questions(
       "Quem escreveu 'Dom Quixote'?\n"
       "A) Miguel de Cervantes\n"
       "B) William Shakespeare\n"
       "C) Machado de Assis\n"
       "D) Leon Tolstói\n",
       "a"
   )
   question3.ask_question()

   question4 = quiz.Questions(
       "Qual elemento químico tem o símbolo 'O'?\n"
       "A) Ouro\n"
       "B) Oxigênio\n"
       "C) Prata\n"
       "D) Zinco\n",
       "b"
   )
   question4.ask_question()

   question5 = quiz.Questions(
       "Em que ano o homem pisou na Lua pela primeira vez?\n"
       "A) 1965\n"
       "B) 1969\n"
       "C) 1972\n"
       "D) 1980\n",
       "b"
   )
   question5.ask_question()
   #quiz.Questions.final()

if __name__ == '__main__':
    main()


