import sys
sys.path.append('C:\\Users\\User\\OneDrive\\Desktop\\python作業\\W10\\Class')
from PyQt6 import QtCore, QtGui, QtWidgets
from class_init import Ui_MainWindow 

class working:
    def __init__(self,ui):
        self.ui = ui

    def wait(self):
        self._translate = QtCore.QCoreApplication.translate
        self.ui.pushButton.clicked.connect(lambda: self.button_query())
        self.ui.pushButton_2.clicked.connect(lambda: self.button_2_query())
        self.ui.pushButton_3.clicked.connect(lambda: self.button_3_query())
    def button_query(self):
        self.ui.textEdit_2.setEnabled(True)
        self.ui.pushButton_2.setEnabled(True)
        self.ui.textEdit_3.setEnabled(True)
        self.ui.textEdit.setEnabled(False)
        self.ui.pushButton.setEnabled(False)

    def button_2_query(self):
        self.ui.pushButton_3.setEnabled(True)
        self.ui.textEdit_2.setEnabled(False)
        self.ui.pushButton_2.setEnabled(False)
        self.ui.textEdit_3.setEnabled(False)

    def button_3_query(self):
        self.ui.pushButton.setEnabled(True)
        self.ui.textEdit.setEnabled(True)
        self.ui.textEdit.setText
        outdata= {'name':self.ui.textEdit.toPlainText(),
            'scores':{ self.ui.textEdit_2.toPlainText() :self.ui.textEdit_3.toPlainText() }
            } 
        print(outdata)
        outdata= "The information" + str(outdata) + "is sent" 
        self.ui.label_6.setText(self._translate("MainWindow",outdata ))
        


#textEditWidget.toPlainText()

'''
if __name__ == "__main__":s
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())'''
