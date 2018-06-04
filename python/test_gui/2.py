import sys
from PySide import QtCore, QtGui, QtUiTools
#import QtCore

def on_click():
    print("clicketd")


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)

    loader = QtUiTools.QUiLoader()
    uifile = QtCore.QFile("mainwindow.ui")
    uifile.open(QtCore.QFile.ReadOnly)
    MainWindow = loader.load(uifile, None)
    uifile.close()

    MainWindow.connect(MainWindow.button1, QtCore.SIGNAL("clicked()"), on_click)

    MainWindow.show()
    sys.exit(app.exec_())
