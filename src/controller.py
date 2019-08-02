from typing import List, Tuple, Optional

import attr

from question import Question

@attr.s
class QuestionListController:
    """Controler for application"""

    questions: List[Question] = attr.ib()
    """Collection of all questions prepared for test."""

    _current_question: Question = attr.ib(default=attr.Factory(lambda self: self.questions[0], takes_self=True))
    """Question object that is currently processed."""

    counter: int = attr.ib(default=1)
    """Index of question that should be processed next."""

    wrong_points: int = attr.ib(default=0)
    """Number of wrong answers."""

    good_points: int = attr.ib(default=0)
    """Number of good answers."""

    checked: bool = attr.ib(default=False)
    """True if current question has been already checked."""

    completed: bool = attr.ib(default=False)
    """True if we processed all questions and test is completed."""

    @property
    def current_question(self) -> str:
        """Returns text of current question."""
        return self._current_question.question

    @property
    def current_answers(self) -> List[str]:
        """Returns list of all answers."""
        return self._current_question.all_answers
    
    def load_new_question(self) -> None:
        """Loads new question if anything remained or mark test as completed. """
        if self.counter < len(self.questions):
            self._current_question = self.questions[self.counter]
            self.counter += 1
            self.checked = False
        else:
            self.completed = True
            
    def check_answer(self, clicked_answer: str) -> Tuple[Optional[str], Optional[str]]:
        """
        Check which answer has been clicked, counts points and return answers to color.

        First element of returned tuple is answer to color green and second is answer to color red.
        """
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
