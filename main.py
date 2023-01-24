from PyQt6.QtCore import QThread, pyqtSignal, Qt
from PyQt6.QtWidgets import *
from PyQt6.QtWidgets import QLCDNumber
from PyQt6.QtGui import QPixmap
import sys
import pyaudio
import audioop
import keyboard
from kb_input import num_to_pad, pad_scancodes


class AudioThread(QThread):
    volume = pyqtSignal(int)
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100

    def __init__(self):
        super(AudioThread, self).__init__()
        p = pyaudio.PyAudio()
        CHUNK = 1024
        FORMAT = pyaudio.paInt16
        CHANNELS = 1
        RATE = 44100
        self.stream = p.open(format=FORMAT, 
            channels=CHANNELS, 
            rate=RATE,
            input=True,
            frames_per_buffer=CHUNK)

    def run(self):
        while True:
            data = self.stream.read(self.CHUNK)
            rms = audioop.rms(data, 2)
            self.volume.emit(rms)

class Display(QWidget):

    def __init__(self):
        super().__init__()

        self.initAudio()
        self.initNumpad()
        self.initUI()

    def initAudio(self):
        self.audio_thread = AudioThread()
        self.audio_thread.start()
        self.audio_thread.volume.connect(self.displayVolume)


    def displayVolume(self, vol):
        self.disp.display(vol)

        level = int(vol / int(self.attrs["divider"].text())) * float(self.attrs["multiplier"].text())
        self.lbl.move(0, -level)
        #self.lbl.move()



    def initNumpad(self):
        for ps in pad_scancodes:
            print(ps)
            keyboard.hook_key(ps, self.handleNumpad)

    def initUI(self):

        hbox = QHBoxLayout(self)

        # Image Display
        self.pixmap = QPixmap('./images/0.png')
        self.lbl = QLabel(self)
        self.lbl.setPixmap(self.pixmap)
        self.lbl.setStyleSheet('''QWidget{background-color:rgb(0,255,0);}''')
        hbox.addWidget(self.lbl)
        # Volume Display and Control

        self.volume_col = QVBoxLayout(self)

        # volume display
        self.disp = QLCDNumber()
        self.disp.setDigitCount(3)

        settings = {
            "divider": 100,
            "multiplier": 1,
        }
        self.attrs = {}
        for key, value in settings.items():
            lineedit = QLineEdit(self)
            lineedit.setText(str(value))
            self.volume_col.addWidget(lineedit)
            self.attrs[key] = lineedit
        
        self.volume_col.addWidget(self.disp)

        hbox.addLayout(self.volume_col)

        self.setLayout(hbox)

        self.disp.setFocus()

        self.move(300, 200)
        self.setWindowTitle('Sid')
        self.show()

    def handleNumpad(self, event):
        sc = event.scan_code
        # print("Pressed", event.scan_code)
        # print("event: ", event)
        # print("name: ", event.name)
        if event.name not in [str(i) for i in range(10)]:
            return
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