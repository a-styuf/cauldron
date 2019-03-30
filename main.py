import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import QColor, QBrush
import main_win
import mb110_224
import time
import configparser
import os


class MainWindow(QtWidgets.QMainWindow, main_win.Ui_Cauldron):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        #
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        #
        self.devGridLayout = QtWidgets.QGridLayout(self.devGBox)
        self.mb110_widget = mb110_224.MB110_Widget(self, title="МВ110-224.8")
        self.devGridLayout.addWidget(self.mb110_widget, 0, 0, 1, 1)
        #
        self.recreate_log_files()
        self.restartLogPButt.clicked.connect(self.recreate_log_files)
        #
        self.cycle_timer = QtCore.QTimer()
        self.cycle_timer.timeout.connect(self.cycle_body)

        self.startCyclePButt.clicked.connect(self.cycle_start)
        self.stopCyclePButt.clicked.connect(self.cycle_stop)

    def cycle_start(self):
        self.cycle_timer.start(1)
        pass

    def cycle_stop(self):
        self.cycle_timer.stop()
        pass

    def cycle_body(self):
        self.cycle_timer.setInterval(self.periodSBox.value() * 1000)
        # опрос девайсов
        self.mb110_widget.dev.read_temp()
        self.log_file.write(self.mb110_widget.dev.log_data().replace(".", ",") + "\n")
        pass

    # LOGs #
    def create_log_file(self, file=None, prefix="", extension=".csv"):
        dir_name = "Logs"
        sub_dir_name = dir_name + "\\" + time.strftime("%Y_%m_%d", time.localtime()) + " Лог"
        sub_sub_dir_name = sub_dir_name + "\\" + time.strftime("%Y_%m_%d %H-%M-%S ",
                                                               time.localtime()) + "Лог"
        try:
            os.makedirs(sub_sub_dir_name)
        except (OSError, AttributeError) as error:
            pass
        try:
            if file:
                file.close()
        except (OSError, NameError, AttributeError) as error:
            pass
        file_name = sub_sub_dir_name + "\\" + time.strftime("%Y_%m_%d %H-%M-%S ",
                                                            time.localtime()) + prefix + " " + extension
        file = open(file_name, 'a')
        return file

    def recreate_log_files(self):
        self.log_file = self.create_log_file(prefix="термопары")
        self.log_file.write(self.mb110_widget.dev.log_name() + "\n")
        pass

    def close_log_file(self, file=None):
        if file:
            try:
                file.close()
            except (OSError, NameError, AttributeError) as error:
                pass
        pass

    def closeEvent(self, event):
        self.close_log_file(file=self.log_file)
        self.close()
        pass


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    # QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
    # os.environ["QT_SCALE_FACTOR"] = "1.0"
    #
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = MainWindow()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение
