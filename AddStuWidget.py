from PyQt6 import QtWidgets, QtGui, QtCore
from WorkWidgets.WidgetComponents import LabelComponent, LineEditComponent, ButtonComponent


class AddStuWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("add_stu_widget")

        layout = QtWidgets.QGridLayout()

        header_label = LabelComponent(20, "Add Student")
        name_label = LabelComponent(16, "Name: ")
        subject_label = LabelComponent(16, "Subject: ")
        score_label = LabelComponent(16, "Score: ")

        self.name_editor = LineEditComponent()
        self.name_editor.setPlaceholderText("Name")
        self.subject_editor = LineEditComponent()
        self.subject_editor.setPlaceholderText("Subject")
        self.score_editor = LineEditComponent()
        self.score_editor.setPlaceholderText("Score")

        button = ButtonComponent("Confirm")
        button.clicked.connect(self.confirm_action)

        layout.addWidget(header_label, 0, 0, 1, 2)
        layout.addWidget(name_label, 1, 0, 1, 1)
        layout.addWidget(self.name_editor, 1, 1, 1, 1)
        layout.addWidget(subject_label, 2, 0, 1, 1)
        layout.addWidget(self.subject_editor, 2, 1, 1, 1)
        layout.addWidget(score_label, 3, 0, 1, 1)
        layout.addWidget(self.score_editor, 3, 1, 1, 1)
        layout.addWidget(button, 4, 1, 1, 1)

        layout.setColumnStretch(0, 1)
        layout.setColumnStretch(1, 9)

        layout.setRowStretch(0, 1)
        layout.setRowStretch(1, 2)
        layout.setRowStretch(2, 2)
        layout.setRowStretch(3, 2)
        layout.setRowStretch(4, 5)

        self.setLayout(layout)

    def confirm_action(self):
        name = self.name_editor.text()
        subject = self.subject_editor.text()
        score = self.score_editor.text()
        print("Name:", name)
        print("Subject:", subject)
        print("Score:", score)
