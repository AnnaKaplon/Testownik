from PyQt5.QtWidgets import (QWidget, QApplication, QLabel,
                             QHBoxLayout, QVBoxLayout, QButtonGroup,
                             QRadioButton, QPushButton, QGridLayout)
from PyQt5.QtGui import QFont
import PyQt5.QtCore
import sys
from random import shuffle
from GetData import Question, getData


class App(QWidget):
    
    def __init__(self,  questions):
        super().__init__()
        self.questions = questions
        self.current_question = QLabel(self.questions[0].question)
        self.grid = QGridLayout(self)
        self.radio_button_group = QButtonGroup()
        self.check_button = QPushButton('Check')
        self.next_button = QPushButton('Next')
        self.counter = 1
        self.wrong_points = 0
        self.good_points = 0
        self.checked = False
        self.initUI()
        
    def initUI(self):
        self.setGeometry(200, 200, 450, 300)
        self.setWindowTitle('Testownik')
        
        answers = self.questions[0].getAllAnswers()
        shuffle(answers)
        
        question_box = self.createQuestionBox()
        radio_button_box = self.createRadioButtonBox(answers)
        button_box = self.initHBox(self.check_button, self.next_button)
        empty_label = QLabel('')
        empty_label.setMaximumHeight(20)
        
        self.grid.addLayout(question_box, 1, 1)
        self.grid.addLayout(radio_button_box, 2, 1)
        self.grid.addWidget(empty_label, 3, 1)
        self.grid.addLayout(button_box, 5, 1)
        
        self.check_button.clicked.connect(self.onCheckButtonClick)
        self.next_button.clicked.connect(self.onNextButtonClick)
        
        self.show()
        
    def createQuestionBox(self):
        font = QFont()
        font.setPointSize(15)
        self.current_question.setMaximumHeight(50)
        self.current_question.setFont(font)
        return self.initHBox(self.current_question)
    
    def createRadioButtonBox(self, answers):
        radio_button_list = []
        radio_button_box = QVBoxLayout()
        
        for answer in answers:
            radio_button_list.append(QRadioButton(answer))
        for n, button in enumerate(radio_button_list):
            self.radio_button_group.addButton(button, n)
            radio_button_box.addLayout(self.initHBox(button))
        return radio_button_box
    
    def initHBox(self, widget1, widget2=None):
        box = QHBoxLayout()
        box.addStretch()
        box.addWidget(widget1)
        box.addStretch()
        if widget2 != None:
            box.addWidget(widget2)
            box.addStretch()
        return box
        
    def onNextButtonClick(self):
        for button in self.radio_button_group.buttons():
            button.setStyleSheet('color: black')
            
        if self.counter < len(self.questions):
            self.changeQuestion()
            self.counter += 1
            self.checked = False
        else:
            self.current_question.setText('The end!')
            
            for button in self.radio_button_group.buttons():
                button.deleteLater()
           
            points_box = self.createPointsBox()
            self.grid.addLayout(points_box, 2, 1)
            
            self.check_button.setEnabled(False)
            self.next_button.setEnabled(False)
            
            
    def changeQuestion(self):
        answers = self.questions[self.counter].getAllAnswers()
        shuffle(answers)
        
        self.current_question.setText(self.questions[self.counter].question)
        for n, button in enumerate(self.radio_button_group.buttons()):
                button.setText(answers[n])
    
    def createPointsBox(self):
        good_points_label = QLabel('Good answers: ' + str(self.good_points))
        wrong_points_label = QLabel('Wrong answers: ' + str(self.wrong_points))
        return self.initHBox(good_points_label, wrong_points_label)
                    
    def onCheckButtonClick(self):
        answer = self.questions[self.counter - 1].good_answer
        checked_button = self.radio_button_group.checkedButton()
        try:
            checked_button_text = str(self.radio_button_group.checkedButton().text())
        except AttributeError:
            checked_button_text = None
            
        if self.checked == False:
            if checked_button_text == answer:
                checked_button.setStyleSheet('color: green')
                self.good_points += 1
            elif checked_button_text == None:
                self.makeAnswerGreen(answer)
                self.wrong_points += 1
            else:   
                self.makeAnswerGreen(answer)
                checked_button.setStyleSheet('color: red')
                self.wrong_points += 1
        self.checked = True
        
    def makeAnswerGreen(self, answer):
        for button in self.radio_button_group.buttons():
                if  str(button.text()) == answer:
                    button.setStyleSheet('color: green')
        

def main():
    app = QApplication(sys.argv)
    questions = getData()
    ex = App(questions)
    sys.exit(app.exec_())
    
if __name__ == "__main__":
    main()
