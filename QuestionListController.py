from Question import Question, getData

class QuestionListController():

    def __init__(self, questions):
        self.questions = questions
        self.current_question = self.questions[0]
        self.counter = 1
        self.wrong_points = 0
        self.good_points = 0
        self.checked = False
        self.completed = False
        
    def getCurrentQuestion(self):
        return self.current_question.getQuestion()
    
    def getCurrentAnswers(self):
        return self.current_question.getAllAnswers()
    
    def getWrongPoints(self):
        return self.good_points
    
    def getGoodPoints(self):
        return self.wrong_points
    
    def getCompleted(self):
        return self.completed
    
    def loadNewQuestion(self):
        if self.counter < len(self.questions):
            self.current_question = self.questions[self.counter]
            self.counter += 1
        else:
            self.completed = True