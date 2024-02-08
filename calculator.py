import sys #send arguments to the application from command line.
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtGui import QIcon

class Calculator(QMainWindow):
    def __init__(self):
        super(Calculator, self).__init__()
        self.setGeometry(2200,300,700,700)# ilk rakamlar desktopa göre sol üstün konumunu, son iki değer ise windowun boyutunu gösterir
        self.setWindowTitle('Trading Bot') #Başlık
        self.setToolTip('ButterFly 1')
        self.setWindowIcon(QIcon('butterfly.jpg')) # ikon koyma   
        self.initUI()

    def initUI(self):
        #içerisine label koyma
        self.lbl_number1 = QtWidgets.QLabel(self)
        self.lbl_number1.setText('Enter Your Name :')
        self.lbl_number1.move(50,30) # label konumu
    #Text box oluşturalım
        self.txt_number1 = QtWidgets.QLineEdit(self)
        self.txt_number1.move(150, 30)
        self.txt_number1.resize(200, 32)


        #içerisine label koyma
        self.lbl_number2 = QtWidgets.QLabel(self)
        self.lbl_number2.setText('Enter Your SurName :')
        self.lbl_number2.move(50,80) # label konumu     

    #Text box oluşturalım
        self.txt_number2 = QtWidgets.QLineEdit(self)
        self.txt_number2.move(150, 80)
        self.txt_number2.resize(200, 32)


    #buton oluşturma
        self.btn_add = QtWidgets.QPushButton(self)
        self.btn_add.setText('+')
        self.btn_add.move(150, 130)
        self.btn_add.clicked.connect(self.calculate)

    #buton oluşturma
        self.btn_sub = QtWidgets.QPushButton(self)
        self.btn_sub.setText('-')
        self.btn_sub.move(150, 180)
        self.btn_sub.clicked.connect(self.calculate)

    #buton oluşturma
        self.btn_mul = QtWidgets.QPushButton(self)
        self.btn_mul.setText('x')
        self.btn_mul.move(150, 230)
        self.btn_mul.clicked.connect(self.calculate)

    #buton oluşturma
        self.btn_div = QtWidgets.QPushButton(self)
        self.btn_div.setText('/')
        self.btn_div.move(150, 280)
        self.btn_div.clicked.connect(self.calculate)


        self.lbl_result = QtWidgets.QLabel(self)
        self.lbl_result.setText('Result:')
        self.lbl_result.move(150,330)
        self.lbl_result.resize(200,200)
    
    def calculate(self):
        sender = self.sender()
        print(sender.text())
        result = 0
        if sender.text() == '+':
            result = int(self.txt_number1.text()) + int(self.txt_number2.text())
        elif sender.text() == '-':
            result = int(self.txt_number1.text()) - int(self.txt_number2.text())
        elif sender.text() == 'x':
            result = int(self.txt_number1.text()) * int(self.txt_number2.text())
        elif sender.text() == '/':
            result = int(self.txt_number1.text()) / int(self.txt_number2.text())
        self.lbl_result.setText(f'Result : {result}')
  

def window():
    app = QApplication(sys.argv)
    win = Calculator()
    win.show()
    sys.exit(app.exec_()) # x e clicklendiğinde windowu kapat

window()