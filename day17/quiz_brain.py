class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        question_number = self.question_number
        user_answer = input(f"Q.{question_number + 1}: {self.question_list[question_number].text} "
                            f"(True/False) : ").lower()
        self.check_answer(user_answer)
        self.question_number += 1

    def still_has_questions(self):
        return len(self.question_list) > self.question_number

    def check_answer(self, answer):
        correct_answer = self.question_list[self.question_number].answer.lower()
        if answer == correct_answer:
            print("You got it right!")
            self.score += 1
        else:
            print("That's Wrong.")
        print(f"The correct answer was {correct_answer}")
        if not self.question_number + 1 == len(self.question_list):
            print(f"Your current score is {self.score}/{self.question_number + 1}")

