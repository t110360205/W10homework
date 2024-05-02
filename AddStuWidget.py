from PyQt6 import QtWidgets, QtGui, QtCore
from WorkWidgets.WidgetComponents import LabelComponent, LineEditComponent, ButtonComponent


class AddStuWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("add_stu_widget")

        layout = QtWidgets.QGridLayout()

        header_label = LabelComponent(20, "Add Student")
        content_label = LabelComponent(16, "Name: ")
        subject_label = LabelComponent(16, "Subject: ")
        score_label = LabelComponent(16, "Score: ")
        self.editor_label = LineEditComponent("Name")
        self.editor_label.mousePressEvent = self.clear_editor_content
        self.editor_label.textChanged.connect(self.button_control)
        self.subject_label = LineEditComponent("Subject")
        self.score_label = LineEditComponent("Score")
        #self.subject_label.mousePressEvent = self.clear_editor_content
        #self.score_label.mousePressEvent = self.clear_editor_content
        self.subject_label.textChanged.connect(self.button_control)
        self.score_label.textChanged.connect(self.button_control)
        button = ButtonComponent("Send")
        #button.clicked.connect(self.confirm_action)
        self.query_button = ButtonComponent("Query")
        self.add_button = ButtonComponent("Add")  
        self.query_button.clicked.connect(self.print_qurey)
        self.add_button.clicked.connect(self.print_input_text)
        button.clicked.connect(self.send)
        self.text_label = QtWidgets.QLabel("")
        self.text_label.setWordWrap(True)

        layout.addWidget(header_label, 0, 0, 1, 1)
        layout.addWidget(self.text_label, 0, 3, 1, 1)
        layout.addWidget(content_label, 1, 0, 1, 1)
        layout.addWidget(self.editor_label, 1, 1, 1, 1)
        layout.addWidget(self.query_button,1, 2, 1, 1)
        layout.addWidget(subject_label, 2, 0, 1, 1)
        layout.addWidget(self.subject_label, 2, 1, 1, 1)
        layout.addWidget(button, 4, 3, 1, 1)
        layout.addWidget(score_label, 3, 0, 1, 1)
        layout.addWidget(self.score_label, 3, 1, 1, 1)
        layout.addWidget(self.add_button,3, 2, 1, 1)

        layout.setColumnStretch(0, 2)
        layout.setColumnStretch(1, 2)

        layout.setRowStretch(0, 1)
        layout.setRowStretch(1, 4)
        layout.setRowStretch(2, 2)
        layout.setRowStretch(3, 5)

        self.setLayout(layout)

    def button_control(self):
        if self.editor_label.text():
            self.query_button.setDisabled(False)  
        else:
            self.query_button.setDisabled(True)
        if self.subject_label.text() and self.score_label.text():
            self.add_button.setEnabled(True)
        else:
            self.add_button.setEnabled(False)

    def clear_editor_content(self, event):
        self.editor_label.clear()
        #elif event == self.score_label:
            #self.score_label.clear()
        #elif event == self.score_label:
            #self.subject_label.clear()

    def confirm_action(self):
        print(self.editor_label.text())

    def print_qurey(self):
        name = self.editor_label.text()
        text = (f"Please enter subject for student '{name}'")
        self.text_label.setText(text)
    def print_input_text(self):
        name = self.editor_label.text()
        if len(name) == 0 :
            text =(f"Please enter the student's name")
        else:
            subject = self.subject_label.text()
            score = self.score_label.text()
            text = (f"Student {name}'s subject {subject} with score {score} added")
        self.text_label.setText(text)
    def send(self):
        name = self.editor_label.text()
        subject = self.subject_label.text()
        score = self.score_label.text()
        text = {"name":name ,"scores":{subject:score}}
        text1 = (f"The imformation {text} is send")
        self.text_label.setText(text1)