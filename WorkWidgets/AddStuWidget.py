from PyQt6 import QtWidgets, QtGui, QtCore
from WorkWidgets.WidgetComponents import LabelComponent, LineEditComponent, ButtonComponent


class AddStuWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.add_dict={"name":"","scores":{}}
        self.message=LabelComponent(16,"")
        self.setObjectName("add_stu_widget")

        self.layout = QtWidgets.QGridLayout()

        header_label = LabelComponent(20, "Add Student")

        name_label = LabelComponent(16, "Name: ")
        self.editor_name_label = LineEditComponent("Name")
        self.editor_name_label.mousePressEvent = self.editor_name_action
        self.query_button=ButtonComponent("Query")
        self.query_button.clicked.connect(self.query_button_action)
        self.query_button.setEnabled(False)

        subject_label=LabelComponent(16,"Subject: ")
        self.editor_subject_label=LineEditComponent("Subject")
        self.editor_subject_label.setEnabled(False)
        self.editor_subject_label.mousePressEvent = self.editor_subject_action

        score_label=LabelComponent(16,"Score: ")
        self.editor_score_label=LineEditComponent("")
        self.editor_score_label.setMaxLength(3)
        self.editor_score_label.setDisabled(True)
        self.editor_score_label.setEnabled(False)
        self.editor_score_label.mousePressEvent = self.editor_score_action
        
        self.add_button=ButtonComponent("Add")
        self.add_button.clicked.connect(self.add_button_action)
        self.add_button.setEnabled(False)
        
        self.send_button = ButtonComponent("Send")
        self.send_button.clicked.connect(self.send_button_action)
        self.send_button.setEnabled(False)

        self.layout.addWidget(header_label, 0, 0, 1, 2)
        self.layout.addWidget(name_label, 1, 0, 1, 1)
        self.layout.addWidget(self.editor_name_label, 1, 1, 1, 2)
        self.layout.addWidget(self.query_button,1,2,1,1)
        self.layout.addWidget(subject_label,2,0,1,1)
        self.layout.addWidget(self.editor_subject_label,2,1,1,1)
        self.layout.addWidget(score_label,3,0,1,1)
        self.layout.addWidget(self.editor_score_label,3,1,1,1)
        self.layout.addWidget(self.add_button,3,2,1,1)
        self.layout.addWidget(self.send_button, 4, 4, 2, 1)
#
        #self.layout.setColumnStretch(0, 1)
        #self.layout.setColumnStretch(1, 9)
        #self.layout.setColumnStretch(2, 9)
        #self.layout.setColumnStretch(3, 1)
        #self.layout.setColumnStretch(4, 1)

        #self.layout.setRowStretch(0, 1)
        #self.layout.setRowStretch(1, 2)
        #self.layout.setRowStretch(2, 2)
        #self.layout.setRowStretch(3, 2)
        #self.layout.setRowStretch(4, 5)

        self.setLayout(self.layout)
    def editor_name_action(self, event):
        self.editor_name_label.clear()
        self.query_button.setEnabled(True)
        self.add_button.setEnabled(False)
    def editor_subject_action(self,event):
        self.editor_subject_label.clear()
    def editor_score_action(self, event):
        self.add_button.setEnabled(True)
    #button
    def query_button_action(self,layout):

        self.layout.removeWidget(self.message)
        if self.editor_name_label.text()!="":
            self.add_button.setEnabled(True)
            self.editor_score_label.setEnabled(True)
            self.editor_subject_label.setEnabled(True)
            self.editor_name_label.setEnabled(False)
            self.query_button.setEnabled(False)
            self.message_show("This name \""+self.editor_name_label.text()+"\" has not found.")   #詢問database有沒有此資料
        else:
            self.message_show(16,"The name is empty.")

    def add_button_action(self):
        self.layout.removeWidget(self.message)
        if self.editor_subject_label.text()!=""and self.editor_score_label.text()!="":
            self.query_button.setEnabled(False)
            self.send_button.setEnabled(True)


            name=self.editor_name_label.text()
            subject=self.editor_subject_label.text()
            try:
                score=self.editor_score_label.text()
                score=float(score)
                
                self.add_dict['scores'][subject]=score 

                self.message_show(f"Add [{name},{subject},{score}] success")   #詢問database有沒有此資料
                self.editor_score_label.clear()
                self.editor_subject_label.clear()

            except Exception as e:
                self.message_show("Please enter a number!")

            
        else:
            self.message_show("The subject or score is empty.")

    def send_button_action(self):
        self.layout.removeWidget(self.message)
        self.message_show("The information "+str(self.add_dict)+" is sent")
    

    def message_show(self,message):
        self.message=LabelComponent(16,str(message))
        self.message.setStyleSheet("color:red;")
        self.layout.addWidget(self.message,1,3,1,2)
        self.setLayout(self.layout)

        
        
