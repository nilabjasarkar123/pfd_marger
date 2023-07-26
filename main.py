import sys
from PyQt5 import QtWidgets as widg

def window():
    app = widg.QApplication(sys.argv)
    win = widg.QMainWindow()
    win.show()

    sys.exit(app.exec_())

window()