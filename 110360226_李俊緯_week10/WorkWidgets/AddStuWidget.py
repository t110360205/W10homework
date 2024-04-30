from PyQt6 import QtWidgets, QtGui, QtCore
from WorkWidgets.WidgetComponents import LabelComponent, LineEditComponent, ButtonComponent
import json

class AddStuWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("add_stu_widget")

        layout = QtWidgets.QGridLayout()

        header_label = LabelComponent(20, "Add Student")
        name_label = LabelComponent(16, "Name: ")
        self.name_editor_label = LineEditComponent("Name")
        self.name_editor_label.mousePressEvent = self.clear_name_editor_content
        self.query_btn = ButtonComponent("Query", disable=True)
        self.query_btn.clicked.connect(self.query_action)

        sub_label = LabelComponent(16, "Subject: ")
        self.sub_editor_label = LineEditComponent("Subject", disable=True)
        self.sub_editor_label.mousePressEvent = self.clear_subject_editor_content
        
        score_label = LabelComponent(16, "Score: ")
        self.score_editor_label = LineEditComponent("", disable=True)
        self.score_editor_label.setValidator(QtGui.QIntValidator())
        
        self.add_btn = ButtonComponent("Add", disable=True)
        self.add_btn.clicked.connect(self.add_action)

        self.hint_label = LabelComponent(16, "")
        self.hint_label.setStyleSheet("color:red;")
        self.send_btn = ButtonComponent("Send", disable=True)
        self.send_btn.clicked.connect(self.send_action)

        layout.addWidget(header_label, 0, 0, 1, 3)

        layout.addWidget(name_label, 1, 0, 1, 1)
        layout.addWidget(self.name_editor_label, 1, 1, 1, 1)
        layout.addWidget(self.query_btn, 1, 2, 1, 1)

        layout.addWidget(sub_label, 2, 0, 1, 1)
        layout.addWidget(self.sub_editor_label, 2, 1, 1, 1)

        layout.addWidget(score_label, 3, 0, 1, 1)
        layout.addWidget(self.score_editor_label, 3, 1, 1, 1)
        layout.addWidget(self.add_btn, 3, 2, 1, 1)

        layout.addWidget(self.hint_label, 0, 3, 2, 1)
        
        layout.addWidget(self.send_btn, 5, 3, 1, 1)

        layout.setColumnStretch(0, 1)
        layout.setColumnStretch(1, 4)
        layout.setColumnStretch(2, 2)
        layout.setColumnStretch(3, 3)

        layout.setRowStretch(0, 1)
        layout.setRowStretch(1, 2)
        layout.setRowStretch(2, 2)
        layout.setRowStretch(3, 2)
        layout.setRowStretch(4, 4)
        layout.setRowStretch(5, 1)
        self.setLayout(layout)

    def clear_name_editor_content(self, event):
        self.name_editor_label.clear()
        self.query_btn.setDisabled(False)
    
    def clear_subject_editor_content(self, event):
        self.sub_editor_label.clear()
        self.add_btn.setDisabled(False)

    def clear_all(self):
        self.query_btn.setDisabled(True)
        self.add_btn.setDisabled(True)

        self.sub_editor_label.setDisabled(True)
        self.sub_editor_label.setText("Subject")
        self.score_editor_label.setDisabled(True)
        self.score_editor_label.setText("")

        self.name_editor_label.setText("Name")
        self.name_editor_label.setDisabled(False)

    def query_action(self):
        text = "Please enter subjects for student '{}'".format(self.name_editor_label.text())
        self.hint_label.setText(text)
        print(text)
        self.query_btn.setDisabled(True)
        self.name_editor_label.setReadOnly(True)
        self.sub_editor_label.setDisabled(False)
        self.score_editor_label.setDisabled(False)
        
    
    def add_action(self):
        text = "Student {}'s subject '{}' with score '{}' added"\
                .format(self.name_editor_label.text(), self.sub_editor_label.text(), self.score_editor_label.text())
        self.hint_label.setText(text)
        print(text)
        self.send_btn.setDisabled(False)

    def send_action(self):
        studect = {'name':self.name_editor_label.text(), \
                   'scores':{self.sub_editor_label.text():self.score_editor_label.text()}}
        text = "The information {} is sent.".format(json.dumps(studect))
        self.hint_label.setText(text)
        print(text)
        self.clear_all()
