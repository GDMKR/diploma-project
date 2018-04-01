from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QWidget, QFileDialog, QListWidget
from matplotlib.backends.backend_qt5 import NavigationToolbar2QT as NavigationToolbar

from canvas import MyFigureCanvas


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        MainWindow.setObjectName("Clustering")
        MainWindow.resize(1000, 650)
        MainWindow.setFixedSize(MainWindow.size())

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidgetUI()

        # Layout for graphs
        self.verticalPlotLayout = QVBoxLayout()
        self.verticalPlotLayoutUI()

        # Main horizontal layout firh graph and controller
        self.horizontalLayout.addLayout(self.verticalPlotLayout,4)

        # Layout for controller (right side)
        self.verticalControlLayout = QVBoxLayout()
        self.verticalControlLayout.setObjectName("verticalLayout")

        # Widget for stack with all methods and their controllers
        self.controlWidget = QWidget()

        # Widget(list) with all metgods' names
        self.methodsList = QListWidget()
        self.nameMethodsUI()

        # Controllers for each of methods
        self.stack1 = QWidget()
        self.stack2 = QWidget()
        self.stack3 = QWidget()

        self.stack1UI()
        self.stack2UI()
        self.stack3UI()

        # Stack
        self.Stack = QStackedWidget(self.controlWidget)
        self.StackUI()

        self.controlWidget.setLayout(self.verticalControlLayout)

        self.verticalControlLayout.addWidget(self.methodsList)
        self.verticalControlLayout.addWidget(self.Stack)

        # widget for way to  file
        self.horizontalFileLayout = QHBoxLayout()
        self.fileUI()

        # widget for build button
        self.pushBuildButton = QPushButton(self.horizontalLayoutWidget)
        self.buildButtonUI()

        self.horizontalLayout.addWidget(self.controlWidget, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        # self.menubar = QMenuBar(MainWindow)
        # self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        # self.menubar.setObjectName("menubar")
        # MainWindow.setMenuBar(self.menubar)
        # self.statusbar = QStatusBar(MainWindow)
        # self.statusbar.setObjectName("statusbar")
        # MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Clustering"))
        self.pushBuildButton.setText(_translate("MainWindow", "Build"))

    def horizontalLayoutWidgetUI(self):
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 980, 600))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")

        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")

    def verticalPlotLayoutUI(self):
        self.verticalPlotLayout.setObjectName("verticalLayout")
        self.drawing_widget = QWidget()
        self.canvas = MyFigureCanvas(self.drawing_widget, width=4, height=3, dpi=180)
        self.navi_toolbar = NavigationToolbar(self.canvas,
                                              self.centralwidget)  # createa navigation toolbar for our plot canvas
        self.verticalPlotLayout.addWidget(self.navi_toolbar)
        self.verticalPlotLayout.addWidget(self.drawing_widget)

    def buildNewGraphic(self):
        if self.Stack.currentIndex() == 0:
            self.canvas.KMeans(self.lineEditNOC.text(), self.lineEditFile.text())
        if self.Stack.currentIndex() == 1:
            self.canvas.DBSCAN(self.lineEditEps.text(), self.lineEditMinSamples.text(), self.lineEditFile.text())
        if self.Stack.currentIndex() == 2:
            self.canvas.AffinityPropagation(self.lineEditFile.text())

    def nameMethodsUI(self):
        self.methodsList.insertItem(0, 'K-Means')
        self.methodsList.insertItem(1, 'DBSCAN')
        self.methodsList.insertItem(2, 'Affinity propagation')
        self.methodsList.currentRowChanged.connect(self.display)


    def stack1UI(self):
        self.KMeansForm = QFormLayout()
        self.lineEditNOC = QLineEdit()
        self.KMeansForm.addRow("Number of clusters", self.lineEditNOC)
        self.stack1.setLayout(self.KMeansForm)

    def stack2UI(self):

        DBSCANForm = QFormLayout()
        self.lineEditEps = QLineEdit();
        DBSCANForm.addRow("Eps", self.lineEditEps)
        self.lineEditMinSamples = QLineEdit()
        DBSCANForm.addRow("Min_saples", self.lineEditMinSamples)
        self.stack2.setLayout(DBSCANForm)

    def stack3UI(self):
        AffinityPropagationForm = QFormLayout()
        self.stack3.setLayout(AffinityPropagationForm)

    def display(self, i):
        self.Stack.setCurrentIndex(i)

    def StackUI(self):
        self.Stack.addWidget(self.stack1)
        self.Stack.addWidget(self.stack2)
        self.Stack.addWidget(self.stack3)

    def fileUI(self):
        self.horizontalFileLayout = QHBoxLayout()
        self.lineEditFile = QLineEdit()
        self.browseButton = QPushButton(self.horizontalLayoutWidget)
        self.browseButton.clicked.connect(lambda: self.selectFile())
        self.horizontalFileLayout.addWidget(self.lineEditFile)
        self.horizontalFileLayout.addWidget(self.browseButton)
        self.verticalControlLayout.addLayout(self.horizontalFileLayout)

    def selectFile(self):
        self.lineEditFile.setText(QFileDialog.getOpenFileName()[0])

    def buildButtonUI(self):
        self.pushBuildButton.setObjectName("pushBuildButton")
        self.pushBuildButton.clicked.connect(lambda: self.buildNewGraphic())
        self.verticalControlLayout.addWidget(self.pushBuildButton)
