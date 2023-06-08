from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
QUESTION_FONT = ("Ariel", 20, "italic")

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):

        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quzzler")
        self.window.config(bg = THEME_COLOR, padx=20, pady=20)

        # Create score label
        self.score_label = Label(text = "Score: 0")
        self.score_label.config(fg="white", bg = THEME_COLOR)
        self.score_label.grid(column=2, row = 1)

        # Question Canvas Creation
        self.question_canvas = Canvas(width=300, height=250)
        self.question_text = self.question_canvas.create_text(150, 125, 
                                                              text=" ", 
                                                              font = QUESTION_FONT,
                                                              width= 280)
        self.question_canvas.grid(column=1, row = 2, columnspan=2, pady=30)
        
        # Button Canvas Creation
        right_img = PhotoImage(file = "100Day Python Bootcamp/Day 34 Quiz App/images/true.png")
        wrong_img = PhotoImage(file = "100Day Python Bootcamp/Day 34 Quiz App/images/false.png")
        self.right_button = Button(image=right_img, highlightthickness=0, command=self.check_answer_true)
        self.wrong_button = Button(image=wrong_img, highlightthickness=0, command=self.check_answer_false)
        self.right_button.grid(column=1, row=3)
        self.wrong_button.grid(column=2, row=3)

        self.next_question()

        self.window.mainloop()

    def next_question(self):
        self.score_label.config(text = f"Score: {self.quiz.score}")
        self.question_canvas.config(bg = "white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.question_canvas.itemconfig(self.question_text, text = q_text)
        else:
            self.question_canvas.itemconfig(self.question_text, text = f"Your Final Score: {self.quiz.score}/{self.quiz.question_number}")

    def check_answer_true(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def check_answer_false(self):
        self.give_feedback(is_right = self.quiz.check_answer("False"))
    
    def give_feedback(self, is_right):
        if is_right:
            self.question_canvas.config(bg = "green")
        else:
            self.question_canvas.config(bg = "red")
        self.window.after(1000, self.next_question)
