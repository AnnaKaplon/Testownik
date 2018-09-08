from Question import Question, getData

class QuestionListController()

	def __init__(self, questions):
		self.questions = questions
        self.counter = 1
        self.wrong_points = 0
        self.good_points = 0
        self.checked = False
		
	