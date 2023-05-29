class  QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        answer = input(f"Q{self.question_number+1}: {self.question_list[self.question_number].text} (True/False): ").lower()
        self.check_answer(answer, self.question_list[self.question_number].answer.lower())
        print(f"The correct answer is {self.question_list[self.question_number].answer}.")

        self.question_number += 1
        print(f"Your current score is {self.score}/{self.question_number}")

    def still_have_questions(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False
        
    def check_answer(self, answer, correct_answer):
        if answer == correct_answer:
            self.score += 1
            print("You got this right!")
        else:
            print("Sorry, this is wrong.")