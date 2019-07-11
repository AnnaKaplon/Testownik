from random import shuffle

import easygui
import pandas as pd


class Question:

    def __init__(self, question, good_answer, wrong_answers):
        self.question = question
        self.good_answer = good_answer
        self.wrong_answers = wrong_answers

    @property
    def all_answers(self):
        return [self.good_answer] + self.wrong_answers


def get_data():
    path = easygui.fileopenbox()
    df = pd.read_csv(path, encoding='utf-8')

    questions = []
    for _, row in df.iterrows():
        wrong_answers_list = [answer for (key, answer) in row.items() if key != 'question' and key != 'good_answer']
        questions.append(Question(row['question'], row['good_answer'], wrong_answers_list))

    shuffle(questions)
    return questions
