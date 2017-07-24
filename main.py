from PyQt5.QtWidgets import *

from newApp import Ui_MainWindow

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())




# from app import ApplicationWindow

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#
#     aw = ApplicationWindow()
#     aw.setWindowTitle("Clustering")
#     aw.show()
#
#     # sys.exit(qApp.exec_())
#     app.exec_()