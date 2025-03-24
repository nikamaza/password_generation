from PyQt5 import uic
from PyQt5.QtWidgets import QProgressBar, QWidget, QApplication, QPushButton, QLabel, QListWidget, QLineEdit, QTextEdit, QToolTip, QMessageBox
from PyQt5.QtGui import QPixmap 
from PyQt5.QtCore import QCoreApplication, Qt
import os.path
import random
import sys

app = QApplication([])
ui = uic.loadUi('win.ui')
ui.setWindowTitle("Ocean of keys")
ui.setFixedSize(1161,721)

qp= QPixmap('fon.jpg')
ui.label_3.setPixmap(qp)
ui.show()

def ran_par():
	pas = ''
	for x in range(15): #Количество символов (16)
   		pas = pas + random.choice(list('1234567890abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ'))
	ui.lineEdit.setText(pas)
 
ui.label_6.hide()
ui.label_7.hide()

def par():
	
	parol = ui.lineEdit.text()
	if len(parol)<4:
		ui.label_7.show()
		parol = ''
		ui.label_6.hide()
	else:
		ui.label_6.show()
		ui.label_7.hide()
		soc = ui.lineEdit_2.text()
		my_file = open("passwords.txt", "a+")
		my_file.write(soc +": "+ parol+"\n")
		my_file.close()

ui.pushButton.clicked.connect(par)    
ui.pushButton_2.clicked.connect(ran_par)
app.exec()
