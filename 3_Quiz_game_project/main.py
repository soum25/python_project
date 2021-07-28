# coding:utf-8

from data import question_data
from question_model import Questions
from quiz_brain import Quizbrain

question_bank = []

for each_line in question_data:
    question_1 = each_line["text"]
    answer_1 = each_line["answer"]
    new_question = Questions(question_1, answer_1)
    question_bank.append(new_question)

quiz = Quizbrain(question_bank)

while quiz.still_have_a_question():
    quiz.next_question()

print(f"You finished the quiz and your final score is {quiz.score}/{quiz.question_number}")