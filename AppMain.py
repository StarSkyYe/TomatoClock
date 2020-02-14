import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QIcon
from clockWidget import QClockWidget


def main():
    app = QApplication(sys.argv)
    icon = QIcon(":/icons/images/Tomato.ico")
    app.setWindowIcon(icon)
    clock_widget = QClockWidget()
    clock_widget.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
