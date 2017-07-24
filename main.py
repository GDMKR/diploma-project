import sys
from PyQt5.QtWidgets import QApplication

from app import ApplicationWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)

    aw = ApplicationWindow()
    aw.setWindowTitle("Clustering")
    aw.show()

    # sys.exit(qApp.exec_())
    app.exec_()