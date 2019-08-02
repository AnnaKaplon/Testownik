from random import shuffle
from typing import List

import attr
import easygui
import pandas as pd


@attr.s
class Question:

    question: str = attr.ib()
    """Text of question."""

    good_answer: str = attr.ib()

    wrong_answers: List[str] = attr.ib()

    @property
    def all_answers(self):
        return [self.good_answer] + self.wrong_answers


def get_data():
    path = easygui.fileopenbox()
    df = pd.read_csv(path, encoding='utf-8')

    questions = []
    for _, row in df.iterrows():
        wrong_answers_list = [answer for (key, answer) in row.items() if key != 'question' and key != 'good_answer']
        questions.append(Question(
            question=row['question'],
            good_answer=row['good_answer'],
            wrong_answers=wrong_answers_list)
        )

    shuffle(questions)
    return questions
