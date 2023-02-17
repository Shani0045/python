from PyQt5.QtGui import *
from PyQt5.QtWidgets import*
from PyQt5.QtCore import Qt
app=QApplication([])
win=QWidget()
win.setWindowTitle("DMS")
win.setFixedSize(900,600)
icon=QIcon('truck1.png')
win.setWindowIcon(icon)
grid=QHBoxLayout()
label=QLabel("Welcome to Desktop App")
label2=QLabel("Welcome to Desktop App")
label.setStyleSheet(
    "background-color:blue;"+
    "color:white;"+
    "font-size:20px;"+
    "border:5px solid black;"
)
label.setAlignment(Qt.AlignHCenter)
btn=QPushButton()
btn.setText("Click Me")
btn.setStyleSheet(
    "background-color:blue;"+
    "color:white;"+
    "font-size:20px;"+
    "border:2px solid black;"+
    "border-radius:100px;"
)
grid.addWidget(btn)
grid.addWidget(label)
label2.setStyleSheet(
    "background-color:blue;"+
    "color:white;"+
    "font-size:20px;"+
    "border:5px solid black;"
)
label2.setAlignment(Qt.AlignHCenter)
grid.addWidget(label2)
win.setLayout(grid)

win.show()
app.exec_()