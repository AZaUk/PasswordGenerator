import sys
from random import choice
from PyQt5 import QtCore, QtGui, QtWidgets

bg_ltrs = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
           'W', 'X', 'Y', 'Z']
sml_ltrs = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
nmbrs = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
smbls = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '`', '~', '|', ']', '}', '[', '{']
full_pass = []
full_pass = full_pass + bg_ltrs
full_pass = full_pass + sml_ltrs
full_pass = full_pass + nmbrs

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        MainWindow.setStyleSheet("background-color: rgb(255, 242, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        # Main text - Password Generator
        self.m_t_psgn = QtWidgets.QLabel(self.centralwidget)
        self.m_t_psgn.setGeometry(QtCore.QRect(200, 50, 400, 50))
        self.m_t_psgn.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.m_t_psgn.setStyleSheet("font: 20pt \"Comic Sans MS\";")
        self.m_t_psgn.setAlignment(QtCore.Qt.AlignCenter)
        self.m_t_psgn.setObjectName("m_t_psgn")
        # Output
        self.output = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.output.setGeometry(QtCore.QRect(150, 480, 475, 55))
        self.output.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                  "border: 2px solid black;\n"
                                  "font: 15pt \"Comic Sans MS\";")
        self.output.setObjectName("output")
        # button
        self.gnrt_btn = QtWidgets.QPushButton(self.centralwidget)
        self.gnrt_btn.setGeometry(QtCore.QRect(210, 400, 375, 65))
        self.gnrt_btn.setStyleSheet("font: 20pt \"Comic Sans MS\";\n"
                                    "border: 2px solid black;")
        self.gnrt_btn.setObjectName("gnrt_btn")
        self.gnrt_btn.clicked.connect(self.on_click)
        # Text "By Sealzi"
        self.t_b_slz = QtWidgets.QLabel(self.centralwidget)
        self.t_b_slz.setGeometry(QtCore.QRect(520, 87, 100, 30))
        self.t_b_slz.setStyleSheet("font: 10pt \"Comic Sans MS\";\n"
                                   "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));")
        self.t_b_slz.setAlignment(QtCore.Qt.AlignCenter)
        self.t_b_slz.setObjectName("t_b_slz")
        # Capital letters
        self.cptl_t = QtWidgets.QLabel(self.centralwidget)
        self.cptl_t.setGeometry(QtCore.QRect(150, 140, 360, 30))
        self.cptl_t.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.cptl_t.setStyleSheet("font: 13pt \"Comic Sans MS\";")
        self.cptl_t.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.cptl_t.setObjectName("cptl_t")
        # CApital letters check box
        self.chck_bx_cl = QtWidgets.QCheckBox(self.centralwidget)
        self.chck_bx_cl.setGeometry(QtCore.QRect(550, 150, 50, 20))
        self.chck_bx_cl.setText("")
        self.chck_bx_cl.setObjectName("chck_bx_cl")
        self.chck_bx_cl.setChecked(True)
        # Lowercase letters
        self.lwrcs_t = QtWidgets.QLabel(self.centralwidget)
        self.lwrcs_t.setGeometry(QtCore.QRect(150, 190, 390, 30))
        self.lwrcs_t.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lwrcs_t.setStyleSheet("font: 13pt \"Comic Sans MS\";")
        self.lwrcs_t.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.lwrcs_t.setObjectName("lwrcs_t")
        # lowercase letters checkbox
        self.chck_bx_ll = QtWidgets.QCheckBox(self.centralwidget)
        self.chck_bx_ll.setGeometry(QtCore.QRect(550, 200, 50, 20))
        self.chck_bx_ll.setText("")
        self.chck_bx_ll.setObjectName("chck_bx_ll")
        self.chck_bx_ll.setChecked(True)
        # numbers
        self.nmbrs_t = QtWidgets.QLabel(self.centralwidget)
        self.nmbrs_t.setGeometry(QtCore.QRect(150, 240, 350, 30))
        self.nmbrs_t.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.nmbrs_t.setStyleSheet("font: 13pt \"Comic Sans MS\";")
        self.nmbrs_t.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.nmbrs_t.setObjectName("nmbrs_t")
        # numbers checkbox
        self.chck_bx_n = QtWidgets.QCheckBox(self.centralwidget)
        self.chck_bx_n.setGeometry(QtCore.QRect(550, 250, 50, 20))
        self.chck_bx_n.setText("")
        self.chck_bx_n.setObjectName("chck_bx_n")
        self.chck_bx_n.setChecked(True)
        # symbols checkbox
        self.chck_bx_s = QtWidgets.QCheckBox(self.centralwidget)
        self.chck_bx_s.setGeometry(QtCore.QRect(550, 300, 50, 20))
        self.chck_bx_s.setText("")
        self.chck_bx_s.setObjectName("chck_bx_s")
        # symbols
        self.symbls_t = QtWidgets.QLabel(self.centralwidget)
        self.symbls_t.setGeometry(QtCore.QRect(150, 290, 350, 30))
        self.symbls_t.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.symbls_t.setStyleSheet("font: 13pt \"Comic Sans MS\";")
        self.symbls_t.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.symbls_t.setObjectName("symbls_t")
        # Choose pass length
        self.cpslngth = QtWidgets.QLabel(self.centralwidget)
        self.cpslngth.setGeometry(QtCore.QRect(150, 340, 350, 30))
        self.cpslngth.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.cpslngth.setStyleSheet("font: 13pt \"Comic Sans MS\";")
        self.cpslngth.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.cpslngth.setObjectName("cpslngth")
        # Pass length nmbr
        self.ps_lngth_nmbr = QtWidgets.QSpinBox(self.centralwidget)
        self.ps_lngth_nmbr.setGeometry(QtCore.QRect(550, 350, 50, 30))
        self.ps_lngth_nmbr.setStyleSheet("font: 10pt \"Comic Sans MS\";\n"
                                         "background-color: rgb(255, 255, 255);\n"
                                         "border: 2px solid black;")
        self.ps_lngth_nmbr.setObjectName("ps_lngth_nmbr")
        self.ps_lngth_nmbr.setMinimum(4)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Password Generator by Sealzi"))
        self.m_t_psgn.setText(_translate("MainWindow", "Password Generator"))
        self.gnrt_btn.setText(_translate("MainWindow", "Generate"))
        self.t_b_slz.setText(_translate("MainWindow", "By Sealzi"))
        self.cptl_t.setText(_translate("MainWindow", "Include capital letters? (A,B..."))
        self.lwrcs_t.setText(_translate("MainWindow", "Include lowercase letters? (a,b..."))
        self.nmbrs_t.setText(_translate("MainWindow", "Include numbers? (1,2,3..."))
        self.symbls_t.setText(_translate("MainWindow", "Include symbols? (!,@,#..."))
        self.cpslngth.setText(_translate("MainWindow", "Choose password length"))

    def on_click(self):
        rng = self.ps_lngth_nmbr.value()
        r = 0
        rw = []
        delete = ['[', "'", ',', ']']
        while r != rng:
            chois = choice(full_pass)
            r += 1
            rw.append(chois)
        for d in delete:
            rw = str(rw).replace(d, '')
            rw = rw.replace(" ", "")
        self.output.insertPlainText("It's --  " + str(rw))
        print("It's --  " + str(rw))


app = QtWidgets.QApplication(sys.argv)
app_icon = QtGui.QIcon()
app_icon.addFile("passgen-logo2.png")
app.setWindowIcon(app_icon)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())
