from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QWidget, QFileDialog

from canvas import MyFigureCanvas
from matplotlib.backends.backend_qt5 import NavigationToolbar2QT as NavigationToolbar


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Clustering")
        MainWindow.resize(630, 400)
        MainWindow.setFixedSize(MainWindow.size())

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 600, 400))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")

        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.verticalPlotLayout = QtWidgets.QVBoxLayout()
        self.verticalPlotLayout.setObjectName("verticalLayout")
        self.drawing_widget = QWidget()
        self.canvas = MyFigureCanvas(self.drawing_widget, width=4, height=3, dpi=90)
        self.navi_toolbar = NavigationToolbar(self.canvas,self.centralwidget)  # createa navigation toolbar for our plot canvas
        self.verticalPlotLayout.addWidget(self.navi_toolbar)
        self.verticalPlotLayout.addWidget(self.drawing_widget)

        self.horizontalLayout.addLayout(self.verticalPlotLayout)

        self.verticalControlLayout = QtWidgets.QVBoxLayout()
        self.verticalControlLayout.setObjectName("verticalLayout")


        self.horizontalGraphTypeLayout = QtWidgets.QHBoxLayout()
        self.comboBoxTypeLabel = QtWidgets.QLabel("Type of graph :")
        self.comboBoxType = QtWidgets.QComboBox()
        self.comboBoxType.addItem("Not selected")
        self.comboBoxType.addItem("Clustering")
        self.horizontalGraphTypeLayout.addWidget(self.comboBoxTypeLabel)
        self.horizontalGraphTypeLayout.addWidget(self.comboBoxType)
        self.verticalControlLayout.addLayout(self.horizontalGraphTypeLayout)

        self.horizontalMethodTypeLayout = QtWidgets.QHBoxLayout()
        self.comboBoxMethodLabel = QtWidgets.QLabel("Method :")
        self.comboBox = QtWidgets.QComboBox()
        self.comboBox.addItem("Not selected")
        self.comboBox.addItem("K-Means")
        self.horizontalMethodTypeLayout.addWidget(self.comboBoxMethodLabel)
        self.horizontalMethodTypeLayout.addWidget(self.comboBox)
        self.verticalControlLayout.addLayout(self.horizontalMethodTypeLayout)

        self.horizontalNumberOfClustersLayout = QtWidgets.QHBoxLayout()
        self.lineEditNOCLabel = QtWidgets.QLabel("Number of clusters :")
        self.lineEditNOC= QtWidgets.QLineEdit()
        self.lineEditNOC.setText("4")
        self.horizontalNumberOfClustersLayout.addWidget(self.lineEditNOCLabel)
        self.horizontalNumberOfClustersLayout.addWidget(self.lineEditNOC)
        self.verticalControlLayout.addLayout(self.horizontalNumberOfClustersLayout)

        self.checkBoxNormalize = QtWidgets.QCheckBox("Normalize")
        self.verticalControlLayout.addWidget(self.checkBoxNormalize)

        self.horizontalAxisLayout = QtWidgets.QHBoxLayout()

        self.comboBoxXAxisLabel = QtWidgets.QLabel("X axis :")
        self.comboBoxXAxis = QtWidgets.QComboBox()
        self.comboBoxXAxis.addItem("1")
        self.comboBoxXAxis.addItem("2")
        self.comboBoxXAxis.addItem("3")
        self.comboBoxXAxis.addItem("4")
        self.horizontalAxisLayout.addWidget(self.comboBoxXAxisLabel)
        self.horizontalAxisLayout.addWidget(self.comboBoxXAxis)

        self.comboBoxYAxisLabel = QtWidgets.QLabel("Y axis :")
        self.comboBoxYAxis = QtWidgets.QComboBox()
        self.comboBoxYAxis.addItem("1")
        self.comboBoxYAxis.addItem("2")
        self.comboBoxYAxis.addItem("3")
        self.comboBoxYAxis.addItem("4")
        self.horizontalAxisLayout.addWidget(self.comboBoxYAxisLabel)
        self.horizontalAxisLayout.addWidget(self.comboBoxYAxis)

        self.verticalControlLayout.addLayout(self.horizontalAxisLayout)

        self.horizontalFileLayout = QtWidgets.QHBoxLayout()
        self.lineEditFile = QtWidgets.QLineEdit()
        self.browseButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.browseButton.clicked.connect(lambda: self.selectFile())
        self.horizontalFileLayout.addWidget(self.lineEditFile)
        self.horizontalFileLayout.addWidget(self.browseButton)

        self.verticalControlLayout.addLayout(self.horizontalFileLayout)

        self.pushBuildButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushBuildButton.setObjectName("pushBuildButton")
        self.pushBuildButton.clicked.connect(lambda: self.buildNewGraphic())
        self.verticalControlLayout.addWidget(self.pushBuildButton)

        self.horizontalLayout.addLayout(self.verticalControlLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        # self.menubar = QtWidgets.QMenuBar(MainWindow)
        # self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        # self.menubar.setObjectName("menubar")
        # MainWindow.setMenuBar(self.menubar)
        # self.statusbar = QtWidgets.QStatusBar(MainWindow)
        # self.statusbar.setObjectName("statusbar")
        # MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Clustering"))
        # self.pushButton_2.setText(_translate("MainWindow", "PushButton"))
        # self.pushButton_3.setText(_translate("MainWindow", "PushButton"))
        self.pushBuildButton.setText(_translate("MainWindow", "Build"))
        self.browseButton.setText(_translate("MainWindow", "..."))

    def buildNewGraphic(self):
        if self.comboBox.currentText() == "K-Means":
            self.canvas.rebuildKMeans(self.lineEditNOC.text(), self.comboBoxXAxis.currentText(), self.comboBoxYAxis.currentText(), self.checkBoxNormalize.isChecked(), self.lineEditFile.text())


    def selectFile(self):
        self.lineEditFile.setText(QFileDialog.getOpenFileName()[0])


