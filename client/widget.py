import sys
import wave
import json
import pyaudio
import keyboard

import noisereduce as nr
from scipy.io import wavfile

from PySide6.QtWidgets import QApplication, QWidget
from ui_form import Ui_Widget

from back import recognize_speech, translate


class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

        self.p = pyaudio.PyAudio()  # Create an interface to PortAudio
        self.chunk = 1024  # Record in chunks of 1024 samples
        self.sample_format = pyaudio.paInt16  # 16 bits per sample
        self.channels = 1
        self.fs = 44100  # Record at 44100 samples per second
        self.seconds = 5
        self.frames = []  # Initialize array to store frames
        self.stream = self.p.open(format=self.sample_format,
                                  channels=self.channels,
                                  rate=self.fs,
                                  frames_per_buffer=self.chunk,
                                  input=True)

        self.setWindowTitle("Client")
        self.setLayout(self.ui.formLayout)
        self.bindings()
        self.setup()

    def bindings(self):
        self.ui.record.clicked.connect(self.record)
        self.ui.cancel.clicked.connect(self.stt)
        self.ui.pushButton_2.clicked.connect(self.play)

    def play(self):
        wf = wave.open("client/audio/test.wav", 'rb')


        stream = self.p.open(format=self.p.get_format_from_width(wf.getsampwidth()),
                        channels=wf.getnchannels(),
                        rate=wf.getframerate(),
                        output=True)


        data = wf.readframes(self.chunk)
        while data:
            stream.write(data)
            data = wf.readframes(self.chunk)


        stream.stop_stream()
        stream.close()

    def stt(self):
        #post request STT

        text = recognize_speech("client/audio/test.wav")
        print(text)
        #json_object = json.lo(text)
        output = text["text"]
        self.ui.textEdit.setText(output)

        #post request to translate
        self.ui.textEdit_2.setText(translate(output))

    def setup(self):
        self.ui.textEdit.setReadOnly(True)

    def record(self):
        stream = self.p.open(format=self.sample_format,
                    channels=self.channels,
                    rate=self.fs,
                    input=True,
                    frames_per_buffer=self.chunk)

        print("Recording...")

        frames = []
       
        while True:  # Запись будет продолжаться до остановки
                data = stream.read(self.chunk)
                frames.append(data)
                if keyboard.is_pressed('enter'):  # Проверяем, нажата ли клавиша 'Enter'
                    break

        print("Recording finished.")

        stream.stop_stream()
        stream.close()

        with wave.open("client/audio/test.wav", "wb") as wf:
            wf.setnchannels(self.channels)
            wf.setsampwidth(self.p.get_sample_size(self.sample_format))
            wf.setframerate(self.fs)
            wf.writeframes(b"".join(frames))

        self.remove_noise()

    def remove_noise(self, input_file='client/audio/test.wav', output_file='client/audio/test.wav'):
        rate, data = wavfile.read(input_file)
        reduced_noise = nr.reduce_noise(y=data, sr=rate)
        wavfile.write(output_file, rate, reduced_noise)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
