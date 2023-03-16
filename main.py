# Naming Conventions:  PascalCase    camelCase    snake_case

from question_model import Question
from data import question_data
from question_model import QuizBrain

question_bank = []

for q in question_data:
    question_bank.append(Question(q["text"], q["answer"]))

quiz = QuizBrain(question_bank)


while quiz.still_has_questions():
    quiz.next_question()

print("You have completed the quiz!")
print(f"Your final score was: ({quiz.score}/{quiz.question_number})")