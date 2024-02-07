import sys #send arguments to the application from command line.
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtGui import QIcon

class my_window(QMainWindow):
    def __init__(self):
        super(my_window, self).__init__()
        self.setGeometry(2200,300,700,700)# ilk rakamlar desktopa göre sol üstün konumunu, son iki değer ise windowun boyutunu gösterir
        self.setWindowTitle('Trading Bot') #Başlık
        self.setToolTip('ButterFly 1')
        self.setWindowIcon(QIcon('butterfly.jpg')) # ikon koyma   
        self.initUI()

    def initUI(self):
        #içerisine label koyma
        self.lbl_name = QtWidgets.QLabel(self)
        self.lbl_name.setText('Enter Your Name :')
        self.lbl_name.move(50,50) # label konumu

        #içerisine label koyma
        self.lbl_name = QtWidgets.QLabel(self)
        self.lbl_name.setText('Enter Your SurName :')
        self.lbl_name.move(50,90) # label konumu     
    #Text box oluşturalım
        self.txt_name = QtWidgets.QLineEdit(self)
        self.txt_name.move(200, 50)

    #Text box oluşturalım
        self.txt_surname = QtWidgets.QLineEdit(self)
        self.txt_surname.move(200, 90)

    #buton oluşturma
        self.btn_save = QtWidgets.QPushButton(self)
        self.btn_save.setText('Save')

        #click dinleme
        self.btn_save.clicked.connect(self.clicked)
        self.btn_save.move(200, 130) # koknum

        self.lbl_result = QtWidgets.QLabel(self)
        self.lbl_result.setText('RESULT')
        self.lbl_result.move(200,170)
        self.lbl_result.resize(200,200)
    
    def clicked(self):
        self.lbl_result.setText(f'button clicked\nname : {self.txt_name.text()}\nsurname : {self.txt_surname.text()}')    

def window():
    app = QApplication(sys.argv)
    win = my_window()
    win.show()
    sys.exit(app.exec_()) # x e clicklendiğinde windowu kapat

window()