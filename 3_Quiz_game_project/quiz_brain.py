class Quizbrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_have_a_question(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f" Q.{self.question_number}:{current_question.text} (True/False): \n ")
        self.check_question(user_answer,current_question.answer)

    def check_question(self,user_answer,correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("you got right !")
            self.score += 1
        else:
            print("You got wrong !")
        print(f"the correct answer is {correct_answer}.")
        print(f"Your current score is {self.score}/{self.question_number}")
        print("\n")


