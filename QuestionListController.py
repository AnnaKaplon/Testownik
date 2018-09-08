from Question import Question, getData

class QuestionListController():

    def __init__(self, questions):
        self.questions = questions
        self.current_question = self.questions[0]
        self.counter = 1
        self.wrong_points = 0
        self.good_points = 0
        self.checked = False
        
    def getCurrentQuestion(self):
        return self.current_question.question
    
    def getCurrentAnswers(self):
        return self.current_question.getAllAnswers()