class QuestionListController:

    def __init__(self, questions):
        self.questions = questions
        self._current_question = self.questions[0]
        self.counter = 1
        self.wrong_points = 0
        self.good_points = 0
        self.checked = False
        self.completed = False

    @property
    def current_question(self):
        return self._current_question.question

    @property
    def current_answers(self):
        return self._current_question.all_answers
    
    def load_new_question(self):
        if self.counter < len(self.questions):
            self._current_question = self.questions[self.counter]
            self.counter += 1
            self.checked = False
        else:
            self.completed = True
            
    def check_answer(self, clicked_answer):
        if self.checked:
            return None, None
        
        self.checked = True
        good_answer = self._current_question.good_answer
        
        if clicked_answer == good_answer:
            self.good_points += 1
            return clicked_answer, None
        elif clicked_answer is None:
            self.wrong_points += 1
            return good_answer, None
        else:
            self.wrong_points += 1
            return good_answer, clicked_answer
        
            
            