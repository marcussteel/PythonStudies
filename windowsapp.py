import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon

def window():
    app = QApplication(sys.argv)

#win adında window oluşturalım ve konum, boyutlarını belirleyelim, başlık atalım, ikon koyalım
    win = QMainWindow()

    win.setGeometry(2200,300,700,700)# ilk rakamlar desktopa göre sol üstün konumunu, son iki değer ise windowun boyutunu gösterir
    win.setWindowTitle('Trading Bot') #Başlık
    win.setToolTip('ButterFly 1')
    win.setWindowIcon(QIcon('butterfly.jpg')) # ikon koyma


#içerisine label koyma
    lbl_name = QtWidgets.QLabel(win)
    lbl_name.setText('Enter Your Name :')
    lbl_name.move(50,50) # label konumu

#içerisine label koyma
    lbl_name = QtWidgets.QLabel(win)
    lbl_name.setText('Enter Your SurName :')
    lbl_name.move(50,90) # label konumu

#Text box oluşturalım
    txt_name = QtWidgets.QLineEdit(win)
    txt_name.move(200, 50)

#Text box oluşturalım
    txt_surname = QtWidgets.QLineEdit(win)
    txt_surname.move(200, 90)


    def clicked(self):
        print(f'button clicked\nname : {txt_name.text()}\nsurname : {txt_surname.text()}')

#buton oluşturma
    btn_save = QtWidgets.QPushButton(win)
    btn_save.setText('Save')

    #click dinleme
    btn_save.clicked.connect(clicked)
    btn_save.move(200, 130) # koknum

    
    win.show()
    sys.exit(app.exec_()) # x e clicklendiğinde windowu kapat


window()
