from PyQt6 import QtWidgets, QtCore, QtGui

class LabelComponent(QtWidgets.QLabel):
    def __init__(self, font_size, content):
        super().__init__()

        self.setWordWrap(True)
        self.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)

        self.setFont(QtGui.QFont("Arial", pointSize=font_size, weight=500))
        self.setText(content)


class LineEditComponent(QtWidgets.QLineEdit):
    def __init__(self, default_content="", length=10, width=200, font_size=16, disable=False):
        super().__init__()
        self.setMaxLength(length)
        self.setText(default_content)
        self.setMinimumHeight(30)
        self.setMaximumWidth(width)
        self.setFont(QtGui.QFont("Arial", font_size))
        self.setDisabled(disable)
        self.setStyleSheet("QLineEdit:disabled {background-color:#CDCDCD; color:#B4B4B4; border : 0.5px solid #CDCDCD;}\
                            QLineEdit:enabled, QLineEdit:read-only{background-color:#F2F2F2; color:black; border-width:1px; border-style:solid;}")

class ButtonComponent(QtWidgets.QPushButton):
    def __init__(self, text, font_size=16, disable=False):
        super().__init__()
        self.setText(text)
        self.setFont(QtGui.QFont("Arial", font_size))
        self.setDisabled(disable)
        self.setStyleSheet("QPushButton:disabled {background-color:#CDCDCD;  color:#B4B4B4}\
                            QPushButton:enabled  {background-color:#C8C8C8; color:black;}")
        