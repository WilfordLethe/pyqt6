import sys
from PySide6 import QtWidgets

app = QtWidgets.QApplication(sys.argv)
widget = QtWidgets.QWidget()
widget.resize(800, 480)
widget.setWindowTitle("Hello,PySide6")
widget.show()
sys.exit(app.exec())
