import sys
from random import shuffle

from PyQt5.QtWidgets import (QWidget, QApplication, QLabel,
                             QHBoxLayout, QVBoxLayout, QButtonGroup,
                             QRadioButton, QPushButton, QGridLayout)
from PyQt5.QtGui import QFont

from Question import get_data
from QuestionListController import QuestionListController


class App(QWidget):

    def __init__(self, questions):
        super().__init__()
        self.question_label = QLabel()
        self.grid = QGridLayout(self)
        self.radio_button_group = QButtonGroup()
        self.check_button = QPushButton('Check')
        self.next_button = QPushButton('Next')
        self.controller = QuestionListController(questions)
        self.init_ui()

    def init_ui(self):
        self.setGeometry(200, 200, 450, 300)
        self.setWindowTitle('Testownik')

        answers = self.controller.current_answers
        shuffle(answers)

        question_box = self.create_question_box()
        radio_button_box = self.create_radio_button_box(answers)
        button_box = self.init_hbox(self.check_button, self.next_button)
        empty_label = QLabel('')
        empty_label.setMaximumHeight(20)

        self.grid.addLayout(question_box, 1, 1)
        self.grid.addLayout(radio_button_box, 2, 1)
        self.grid.addWidget(empty_label, 3, 1)
        self.grid.addLayout(button_box, 5, 1)

        self.check_button.clicked.connect(self.on_check_button_click)
        self.next_button.clicked.connect(self.on_next_button_click)

        self.show()

    def create_question_box(self):
        font = QFont()
        font.setPointSize(15)
        self.question_label.setText(self.controller.current_question)
        self.question_label.setMaximumHeight(50)
        self.question_label.setFont(font)
        return self.init_hbox(self.question_label)

    def create_radio_button_box(self, answers):
        radio_button_list = [QRadioButton(answer) for answer in answers]
        radio_button_box = QVBoxLayout()
        for n, button in enumerate(radio_button_list):
            self.radio_button_group.addButton(button, n)
            radio_button_box.addLayout(self.init_hbox(button))
        return radio_button_box

    def init_hbox(self, widget1, widget2=None):
        box = QHBoxLayout()
        box.addStretch()
        box.addWidget(widget1)
        box.addStretch()
        if widget2:
            box.addWidget(widget2)
            box.addStretch()
        return box

    def on_next_button_click(self):
        self.controller.load_new_question()

        if not self.controller.completed:
            for button in self.radio_button_group.buttons():
                button.setStyleSheet('color: black')

            self.change_question()
        else:
            self.question_label.setText('The end!')

            for button in self.radio_button_group.buttons():
                button.deleteLater()

            points_box = self.create_points_box()
            self.grid.addLayout(points_box, 2, 1)

            self.check_button.setParent(None)
            self.next_button.setParent(None)

    def change_question(self):
        answers = self.controller.current_answers
        shuffle(answers)

        self.question_label.setText(self.controller.current_question)
        for n, button in enumerate(self.radio_button_group.buttons()):
            button.setText(answers[n])

    def create_points_box(self):
        good_points_label = QLabel('Good answers: ' + str(self.controller.good_points))
        wrong_points_label = QLabel('Wrong answers: ' + str(self.controller.wrong_points))
        return self.init_hbox(good_points_label, wrong_points_label)

    def on_check_button_click(self):
        try:
            checked_button_text = str(self.radio_button_group.checkedButton().text())
        except AttributeError:
            checked_button_text = None

        [to_make_green, to_make_red] = self.controller.check_answer(checked_button_text)

        if to_make_green is not None:
            self.colour_answer(to_make_green, 'green')
        if to_make_red is not None:
            self.colour_answer(to_make_red, 'red')

    def colour_answer(self, answer, colour):
        for button in self.radio_button_group.buttons():
            if str(button.text()) == answer:
                button.setStyleSheet(f'color: {colour}')


def main():
    app = QApplication(sys.argv)
    questions = get_data()
    ex = App(questions)
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
