class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list

    def next_question(self):
        question_number = self.question_number
        user_answer = input(f"Q.{question_number + 1}: {self.question_list[question_number].text} (True/False)")
