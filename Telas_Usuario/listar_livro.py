# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'listar_livro.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(807, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(350, 30, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.result_buscaLivro = QtWidgets.QTextBrowser(self.centralwidget)
        self.result_buscaLivro.setGeometry(QtCore.QRect(480, 140, 256, 311))
        self.result_buscaLivro.setObjectName("result_buscaLivro")
        self.voltar = QtWidgets.QPushButton(self.centralwidget)
        self.voltar.setGeometry(QtCore.QRect(650, 480, 121, 61))
        self.voltar.setObjectName("voltar")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(51, 191, 311, 51))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.buscTitle = QtWidgets.QLineEdit(self.widget)
        self.buscTitle.setObjectName("buscTitle")
        self.horizontalLayout.addWidget(self.buscTitle)
        self.BottonBTitle = QtWidgets.QPushButton(self.widget)
        self.BottonBTitle.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../Área de Trabalho/images.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BottonBTitle.setIcon(icon)
        self.BottonBTitle.setObjectName("BottonBTitle")
        self.horizontalLayout.addWidget(self.BottonBTitle)
        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(51, 261, 311, 41))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.widget1)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.buscaAutor = QtWidgets.QLineEdit(self.widget1)
        self.buscaAutor.setObjectName("buscaAutor")
        self.horizontalLayout_2.addWidget(self.buscaAutor)
        self.BottonBAutor = QtWidgets.QPushButton(self.widget1)
        self.BottonBAutor.setText("")
        self.BottonBAutor.setIcon(icon)
        self.BottonBAutor.setObjectName("BottonBAutor")
        self.horizontalLayout_2.addWidget(self.BottonBAutor)
        self.widget2 = QtWidgets.QWidget(self.centralwidget)
        self.widget2.setGeometry(QtCore.QRect(53, 310, 311, 61))
        self.widget2.setObjectName("widget2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.widget2)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.BuscaISBN = QtWidgets.QLineEdit(self.widget2)
        self.BuscaISBN.setObjectName("BuscaISBN")
        self.horizontalLayout_3.addWidget(self.BuscaISBN)
        self.bottonBisbn = QtWidgets.QPushButton(self.widget2)
        self.bottonBisbn.setText("")
        self.bottonBisbn.setIcon(icon)
        self.bottonBisbn.setObjectName("bottonBisbn")
        self.horizontalLayout_3.addWidget(self.bottonBisbn)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 807, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "BUSCA NO ACERVO"))
        self.voltar.setText(_translate("MainWindow", "Voltar"))
        self.label_2.setText(_translate("MainWindow", "Título:"))
        self.label_3.setText(_translate("MainWindow", "Autor:"))
        self.label_4.setText(_translate("MainWindow", "ISBN:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
