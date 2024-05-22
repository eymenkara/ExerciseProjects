from tkinter import *
from quiz_brain import *

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Trivia Quiz")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        # Score Label
        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        # Canvas
        self.canvas = Canvas(bg="white", width=300, height=250)
        self.displayer = self.canvas.create_text(150, 125, text="question", width=280,
                                                 font=("Arial", 20, "italic"), fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # Buttons
        self.true_img = PhotoImage(file="images/true.png")
        self.correct_button = Button(width=100, height=97, image=self.true_img, highlightthickness=0,
                                     command=self.chose_true)
        self.correct_button.grid(row=2, column=0)

        self.false_img = PhotoImage(file="images/false.png")
        self.wrong_button = Button(width=100, height=97, image=self.false_img, highlightthickness=0,
                                   command=self.chose_false)
        self.wrong_button.grid(row=2, column=1)

        self.get_next_question()


        self.window.mainloop()

    # Functions
    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfigure(self.displayer, text=q_text)
        else:
            self.canvas.itemconfig(self.displayer, text="You have reached the end!")
            self.correct_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def chose_true(self):
        self.give_feedback(self.quiz.check_answer(user_answer="True"))

    def chose_false(self):
        self.give_feedback(self.quiz.check_answer(user_answer="False"))

    def give_feedback(self, is_right: bool):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)


