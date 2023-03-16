class Question:

    def __init__(self, text, answer):
        self.text = text
        self.answer = answer


class QuizBrain:

    def __init__(self, q_data):
        self.question_number = 0
        self.question_list = q_data
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        user_answer = input(f"Q-{self.question_number + 1}: {current_question.text} (True/False): ")
        current_answer = current_question.answer
        self.check_answer(user_answer, current_answer)
        self.question_number += 1

    def check_answer(self, user_answer, current_answer):
        if user_answer.lower() == current_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer is {current_answer}")
        print(f"Your score is ({self.score}/{self.question_number + 1})")
        print("\n")

