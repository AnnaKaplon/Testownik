from PyQt5.QtWidgets import (QWidget, QApplication, QLabel,
                             QHBoxLayout, QVBoxLayout, QButtonGroup,
                             QRadioButton, QPushButton, QGridLayout)
from PyQt5.QtGui import QFont
import PyQt5.QtCore
import sys
from random import shuffle
from GetData import Question, getData


class App(QWidget):
    
    def __init__(self, questions):
        super().__init__()
        self.questions = questions
        self.counter = 1
        self.wrongPoints = 0
        self.goodPoints = 0
        self.checked = False
        self.initUI()
        
    def initUI(self):
        self.setGeometry(200, 200, 450, 300)
        self.setWindowTitle('Testownik')
        
        question_box = self.makeQuestionBox()
        
        self.group = QButtonGroup()
        answers = self.questions[0].getAllAnswers()
        radio_button_list = []
        
        for answer in answers:
            radio_button_list.append(QRadioButton(answer))
            
        for n, button in enumerate(radio_button_list):
            self.group.addButton(button, n)
            
        shuffle(radio_button_list)
        
        radio_button_box = QVBoxLayout()
        radio_button_box.setAlignment(PyQt5.QtCore.Qt.AlignCenter)
        
        for button in radio_button_list:
            radio_button_box.addLayout(self.initHBox(button))
        
        empty_label = QLabel('')
        empty_label.setMaximumHeight(20)
        
        self.button1 = QPushButton('Check')
        self.button2 = QPushButton('Next')
        button_box = self.initHBox(self.button1, self.button2)
        
        self.grid = QGridLayout(self)
        self.grid.addLayout(questionBox, 1, 1)
        self.grid.addLayout(radio_button_box, 2, 1)    
        self.grid.addWidget(empty_label, 3, 1)
        self.grid.addLayout(button_box, 5, 1)
        self.grid.setAlignment(PyQt5.QtCore.Qt.AlignRight)
        
        self.button1.clicked.connect(self.onCheckButtonClick)
        self.button2.clicked.connect(self.onNextButtonClick)
        
        self.show()
		
	def makeQuestionBox(self)
		font = QFont()
        font.setPointSize(15)
        
        self.question = QLabel(self.questions[0].question)
        self.question.setMaximumHeight(50)
        self.question.setFont(font)
        return self.initHBox(self.question)
        
    def onNextButtonClick(self):
        
        self.checked = False
        
        for button in self.group.buttons():
            button.setStyleSheet('color: black')
            
        if self.counter < len(self.questions):
            self.question.setText(self.questions[self.counter].question)
            
            answers = self.questions[self.counter].getAllAnswers()
            shuffle(answers)
            
            for n, button in enumerate(self.group.buttons()):
                button.setText(answers[n])
            
            self.counter += 1
            
        else:
            self.question.setText('The end!')
            
            for button in self.group.buttons():
                button.deleteLater()
            
            good_points_label = QLabel('Good answers: ' + str(self.goodPoints))
            wrong_points_label = QLabel('Wrong answers: ' + str(self.wrongPoints))
            
            pointsLayout = self.initHBox(good_points_label, wrong_points_label)
            self.grid.addLayout(pointsLayout, 2, 1)
            
            self.button1.setEnabled(False)
            self.button2.setEnabled(False)
                    
    def onCheckButtonClick(self):
        checked_button = self.group.checkedButton()
        if self.checked == False:
            if str(checked_button.text()) == self.questions[self.counter - 1].good_answer:
                checked_button.setStyleSheet('color: green')
                self.goodPoints += 1
            else:
                for button in self.group.buttons():
                    if str(button.text()) == self.questions[self.counter - 1].good_answer:
                        button.setStyleSheet('color: green')
                checked_button.setStyleSheet('color: red')
                self.wrongPoints += 1
        self.checked = True
        
    def initHBox(self, widget1, widget2=None):
        box = QHBoxLayout()
        box.addStretch()
        box.addWidget(widget1)
        box.addStretch()
        if widget2 != None:
            box.addWidget(widget2)
            box.addStretch()
        return box
        

def main():
    app = QApplication(sys.argv)
    questions = getData()
    ex = App(questions)
    sys.exit(app.exec_())
    
if __name__ == "__main__":
    main()
