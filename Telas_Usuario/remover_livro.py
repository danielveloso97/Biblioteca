# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'remover_livro.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(330, 20, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.layoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_4.setGeometry(QtCore.QRect(102, 289, 311, 61))
        self.layoutWidget_4.setObjectName("layoutWidget_4")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.layoutWidget_4)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_10 = QtWidgets.QLabel(self.layoutWidget_4)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_7.addWidget(self.label_10)
        self.BuscaISBN_2 = QtWidgets.QLineEdit(self.layoutWidget_4)
        self.BuscaISBN_2.setObjectName("BuscaISBN_2")
        self.horizontalLayout_7.addWidget(self.BuscaISBN_2)
        self.bottonBisbn_2 = QtWidgets.QPushButton(self.layoutWidget_4)
        self.bottonBisbn_2.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../Área de Trabalho/images.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bottonBisbn_2.setIcon(icon)
        self.bottonBisbn_2.setObjectName("bottonBisbn_2")
        self.horizontalLayout_7.addWidget(self.bottonBisbn_2)
        self.layoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_3.setGeometry(QtCore.QRect(100, 240, 311, 41))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.layoutWidget_3)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_9 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_6.addWidget(self.label_9)
        self.buscaAutor_2 = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.buscaAutor_2.setObjectName("buscaAutor_2")
        self.horizontalLayout_6.addWidget(self.buscaAutor_2)
        self.BottonBAutor_2 = QtWidgets.QPushButton(self.layoutWidget_3)
        self.BottonBAutor_2.setText("")
        self.BottonBAutor_2.setIcon(icon)
        self.BottonBAutor_2.setObjectName("BottonBAutor_2")
        self.horizontalLayout_6.addWidget(self.BottonBAutor_2)
        self.layoutWidget_5 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_5.setGeometry(QtCore.QRect(100, 170, 311, 51))
        self.layoutWidget_5.setObjectName("layoutWidget_5")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.layoutWidget_5)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_11 = QtWidgets.QLabel(self.layoutWidget_5)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_8.addWidget(self.label_11)
        self.buscTitle_2 = QtWidgets.QLineEdit(self.layoutWidget_5)
        self.buscTitle_2.setObjectName("buscTitle_2")
        self.horizontalLayout_8.addWidget(self.buscTitle_2)
        self.BottonBTitle_2 = QtWidgets.QPushButton(self.layoutWidget_5)
        self.BottonBTitle_2.setText("")
        self.BottonBTitle_2.setIcon(icon)
        self.BottonBTitle_2.setObjectName("BottonBTitle_2")
        self.horizontalLayout_8.addWidget(self.BottonBTitle_2)
        self.result_BL = QtWidgets.QTextBrowser(self.centralwidget)
        self.result_BL.setGeometry(QtCore.QRect(500, 120, 221, 301))
        self.result_BL.setObjectName("result_BL")
        self.voltar = QtWidgets.QPushButton(self.centralwidget)
        self.voltar.setGeometry(QtCore.QRect(500, 464, 131, 61))
        self.voltar.setObjectName("voltar")
        self.excluir_livro = QtWidgets.QPushButton(self.centralwidget)
        self.excluir_livro.setGeometry(QtCore.QRect(660, 464, 131, 61))
        self.excluir_livro.setObjectName("excluir_livro")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
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
        self.label.setText(_translate("MainWindow", "Remover Livro"))
        self.label_10.setText(_translate("MainWindow", "ISBN:"))
        self.label_9.setText(_translate("MainWindow", "Autor:"))
        self.label_11.setText(_translate("MainWindow", "Título:"))
        self.voltar.setText(_translate("MainWindow", "Voltar"))
        self.excluir_livro.setText(_translate("MainWindow", "Excluir"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())