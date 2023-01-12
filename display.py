from PyQt6.QtCore import QThread, pyqtSignal
from PyQt6.QtWidgets import (QWidget, QHBoxLayout,
        QLabel, QApplication, QInputDialog, QMessageBox)
from PyQt6.QtGui import QPixmap
import sys

import keyboard
from kb_input import num_to_pad, pad_scancodes


class Display(QWidget):

    def __init__(self):
        super().__init__()

        self.initNumpad()
        self.initUI()

    def initNumpad(self):
        for ps in pad_scancodes:
            keyboard.hook_key(ps, self.handleNumpad)

    def initUI(self):

        hbox = QHBoxLayout(self)
        self.pixmap = QPixmap('./images/0.png')

        self.lbl = QLabel(self)
        self.lbl.setPixmap(self.pixmap)

        hbox.addWidget(self.lbl)
        self.setLayout(hbox)

        self.move(300, 200)
        self.setWindowTitle('Sid')
        self.show()

    def handleNumpad(self, event):
        sc = event.scan_code
        for num, scan in num_to_pad.items():
            if scan == sc:
                self.pixmap.load(f"./images/{num}.png")
                break
        self.lbl.setPixmap(self.pixmap)
        self.update()


def main():

    app = QApplication(sys.argv)
    ex = Display()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()