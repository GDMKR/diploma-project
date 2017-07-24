# import matplotlib
#
# from canvas import MyFigureCanvas
#
# matplotlib.use("Qt5Agg")
# from PyQt5 import QtCore, QtGui
# from PyQt5.QtWidgets import *
# from matplotlib.backends.backend_qt5 import NavigationToolbar2QT as NavigationToolbar
#
#
# class ApplicationWindow(QMainWindow):
#     def __init__(self):
#         QMainWindow.__init__(self)
#
#
#
#         self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
#
#         self.setWindowTitle("Clustering")
#
#         self.file_menu = QMenu('&File', self)
#         self.file_menu.addAction('&Quit', self.fileQuit,
#                                  QtCore.Qt.CTRL + QtCore.Qt.Key_Q)
#         self.menuBar().addMenu(self.file_menu)
#
#         self.help_menu = QMenu('&Help', self)
#         self.menuBar().addSeparator()
#         self.menuBar().addMenu(self.help_menu)
#
#         self.help_menu.addAction('&About', self.about)
#
#         cb_label = QLabel("Method :")
#         self.cb = QComboBox()
#         self.cb.addItem("Not selected")
#         self.cb.addItem("K-Means")
#
#         startButton = QPushButton("Start")
#         startButton.clicked.connect(lambda : self.buildNewGraphic())
#
#
#         self.drawing_widget = QWidget(self)
#         self.canvas = MyFigureCanvas(self.drawing_widget, width=5, height=4, dpi=100)
#         navi_toolbar = NavigationToolbar(self.canvas, self)  # createa navigation toolbar for our plot canvas
#
#
#
#
#
#         v_box = QVBoxLayout(self.drawing_widget)
#
#         v_box.addWidget(navi_toolbar)
#         v_box.addWidget(self.canvas)
#         v_box.addWidget(startButton)
#         v_box.addWidget(cb_label)
#         v_box.addWidget(self.cb)
#
#
#         self.drawing_widget.setFocus()
#         self.setCentralWidget(self.drawing_widget)
#
#         self.statusBar().showMessage("****", 2000)
#
#     def fileQuit(self):
#         self.close()
#
#     def closeEvent(self, ce):
#         self.fileQuit()
#
#     def buildNewGraphic(self):
#         self.canvas = MyFigureCanvas(self.drawing_widget, width=5, height=4, dpi=100, method= self.cb.currentText())
#         self.canvas.show()
#
#
#
#     def about(self):
#         QMessageBox.about(self, "About",
#                           """about about abput."""
#                           )
#
#
#
#
#
#
