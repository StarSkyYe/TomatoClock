# -*- coding: utf-8 -*-
"""
实现番茄工作时钟的界面逻辑
"""
from PyQt5.QtWidgets import QWidget
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import QTimer
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtCore import QUrl
from ui_Widget import Ui_Widget


class QClockWidget(QWidget):

    STATE_WORK = '工作中...'
    STATE_REST = '休息中...'
    STATE_PEND = '未启动...'

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

        self.timer = QTimer()
        self.timer.stop()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.do_timer_timeout)

        self.lcd_dispaly(self.ui.spinBoxWork.value(), 0)

        self.player = QMediaPlayer()
        self.player.setVolume(30)
        self.change_media_file(self.ui.lineEditAudioFile.text())
        self.player.stateChanged.connect(self.do_player_stateChanged)

        # self.ui.spinBoxWork.setMinimum(1)

    def change_media_file(self, file):
        media_url = QUrl.fromLocalFile(file)
        content = QMediaContent(media_url)
        self.player.setMedia(content)

    def player_play_media(self):
        if self.ui.checkBoxAudio.isChecked():
            self.player.play()

    def player_stop_media(self):
        if self.ui.checkBoxAudio.isChecked():
            self.player.stop()

    def lcd_dispaly(self, min, sec):
        s_minutes = '%02d' % min
        s_seconds = '%02d' % sec
        self.ui.lcdMinutes.display(s_minutes)
        self.ui.lcdSecond.display(s_seconds)

    @pyqtSlot(int)
    def on_spinBoxWork_valueChanged(self, value):
        self.lcd_dispaly(value, 0)

    def on_btnStart_clicked(self):
        self.ui.groupBoxSettings.setEnabled(False)
        self.ui.btnStart.setEnabled(False)
        self.ui.btnStop.setEnabled(True)
        self.ui.labState.setText(self.STATE_WORK)
        value = self.ui.spinBoxWork.value()
        self.lcd_dispaly(value, 0)
        self.timer.start()

    def on_btnStop_clicked(self):
        self.ui.groupBoxSettings.setEnabled(True)
        self.ui.btnStart.setEnabled(True)
        self.ui.btnStop.setEnabled(False)
        self.timer.stop()
        self.ui.labState.setText(self.STATE_PEND)
        self.player_stop_media()

    def on_checkBoxAudio_stateChanged(self, state):
        if state:
            self.ui.lineEditAudioFile.setEnabled(True)
        else:
            self.ui.lineEditAudioFile.setEnabled(False)

    def on_lineEditAudioFile_textChanged(self, text):
        self.change_media_file(text)

    def do_timer_timeout(self):
        current_min = self.ui.lcdMinutes.intValue()
        current_sec = self.ui.lcdSecond.intValue()

        if current_sec == 0:
            current_sec = 59
            if current_min > 0:
                current_min -= 1
            else:
                current_sec = 0
                if self.ui.labState.text() == self.STATE_WORK:
                    self.ui.labState.setText(self.STATE_REST)
                    current_min = self.ui.spinBoxRest.value()
                    self.player_play_media()
                else:
                    self.ui.labState.setText(self.STATE_WORK)
                    current_min = self.ui.spinBoxWork.value()
                    self.player_stop_media()
        else:
            current_sec -= 1

        self.lcd_dispaly(current_min, current_sec)

    def do_player_stateChanged(self, state):
        if state == QMediaPlayer.StoppedState and self.ui.labState.text() == self.STATE_REST:
            self.player_play_media()
