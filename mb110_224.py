import serial
import sys
import serial.tools.list_ports
import minimalmodbus
import time
import threading
import mb110_224_win
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import QColor, QBrush
import os


class MB110_224:
    def __init__(self, **kw):
        # установка или задание параметров по умолчанию
        self.dev_id = ["00A2C238"]
        self.mb_addr = 16
        self.br = 115200
        self.timeout = 0.25
        self.dev_port = ""
        for key in sorted(kw):
            if key == "id":
                self.dev_id = kw.pop(key)
            elif key == "mb_addr":
                self.addr = kw.pop(key)
            elif key == "br":
                self.br = kw.pop(key)
            elif key == "timeout":
                self.timeout = kw.pop(key)
            else:
                pass
        self.state = 0  # состояние
        # попытка подключения при инициализации
        self.instrument = None
        self.state = self._connect_serial_by_ser_num()
        # данные температуры
        self.temp = [0 for i in range(8)]
        self.data_name = ["Время, с",
                          "Канал 1, °С",
                          "Канал 2, °С",
                          "Канал 3, °С",
                          "Канал 4, °С",
                          "Канал 5, °С",
                          "Канал 6, °С",
                          "Канал 7, °С",
                          "Канал 8, °С"]
        self.data = [0 for i in range(len(self.data_name))]
        self.data[0] = time.clock()
        self.graph_data = []
        self.reset_graph_data()
        # поток для чтения
        self.read_thread = threading.Thread(target=self._read_temp)
        self.data_lock = threading.Lock()

    def _connect_serial_by_ser_num(self):  # функция для установки связи с устройством по его dev_id
        com_list = serial.tools.list_ports.comports()
        for com in com_list:
            for serial_number in self.dev_id:
                # print(com.serial_number, serial_number)
                if com.serial_number is not None:
                    if serial_number in com.serial_number:
                        minimalmodbus.BAUDRATE = self.br
                        minimalmodbus.CLOSE_PORT_AFTER_EACH_CALL = True
                        minimalmodbus.TIMEOUT = self.timeout
                        self.dev_port = com.device
                        try:
                            self.instrument = minimalmodbus.Instrument(com.device, self.mb_addr, mode="rtu")
                            self.instrument.debug = False
                            return 1
                        except serial.serialutil.SerialException as error:
                            # print(error)
                            pass
        return -1

    def _read_temp(self):  # функция для запуска в потоке и чтения температуры
        tmp_data = []
        try:
            tmp_data = self.instrument.read_registers(0, 4 * 6)
            time.sleep(0.01)
            tmp_data.extend(self.instrument.read_registers(4 * 6, 4 * 6))
            self.state = 1
        except (serial.serialutil.SerialException, OSError, AttributeError) as error:
            self.state = -1
        self.parc_mb_data(tmp_data)

    def parc_mb_data(self, mb_data):
        temp_list = []
        for i in range(8):
            try:
                temp = mb_data[i*6 + 1] * 10**(-mb_data[i*6 + 0])
                temp_list.append(temp)
            except IndexError:
                temp_list.append(0)
        with self.data_lock:
            self.temp = temp_list
            self.data[0] = time.clock()
            self.data[1:] = self.temp
        return self.temp

    def read_temp(self):
        if self.read_thread.is_alive():
            pass
        else:
            self.read_thread = threading.Thread(target=self._read_temp)
            self.read_thread.start()

    def form_graph_data(self, num=24*3600):
        try:
            for i in range(len(self.data_name)):
                self.graph_data[i][1].append(self.data[i])
                if len(self.graph_data[i][1]) > num:
                    self.graph_data[i][1] = self.graph_data[i][1][-num:]
        except Exception as error:
            # print(error)
            pass

    def reset_graph_data(self):
        self.graph_data = []
        for i in range(len(self.data_name)):
            single_graph = [self.data_name[i], []]
            self.graph_data.append(single_graph)

    def reconnect(self, **kw):
        for key in sorted(kw):
            if key == "id":
                self.dev_id = kw.pop(key)
            elif key == "mb_addr":
                self.addr = kw.pop(key)
            elif key == "br":
                self.br = kw.pop(key)
            elif key == "timeout":
                self.timeout = kw.pop(key)
            else:
                pass
        self.state = self._connect_serial_by_ser_num()
        pass

    def __str__(self):
        tmr_ch_str = "com={1:s};\t" \
                     "{0[0]:.2f};\t{0[1]:.2f};\t{0[2]:.2f};\t{0[3]:.2f};\t"\
                     "{0[4]:.2f};\t{0[5]:.2f};\t{0[6]:.2f};\t{0[7]:.2f};\t"\
            .format(self.data, self.dev_port)
        return tmr_ch_str

    def log_name(self):
        tmr_ch_str = "{0[0]:s};" \
                     "{0[1]:s};{0[2]:s};{0[3]:s};{0[4]:s};" \
                     "{0[5]:s};{0[6]:s};{0[7]:s};{0[8]:s};" \
            .format(self.data_name)
        return tmr_ch_str

    def log_data(self):
        tmr_ch_str = "{0[0]:.3f};" \
                     "{0[1]:.1f};{0[2]:.1f};{0[3]:.1f};{0[4]:.1f};" \
                     "{0[5]:.1f};{0[6]:.1f};{0[7]:.1f};{0[8]:.1f};" \
            .format(self.data)
        return tmr_ch_str


class MB110_Widget(QtWidgets.QFrame, mb110_224_win.Ui_Form):
    def __init__(self, parent, **kw):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        #
        super().__init__(parent)
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        #
        self.title = "MB110"
        for key in sorted(kw):
            if key == "title":
                self.mko_dev = kw.pop(key)
            else:
                pass
        self.devNameLabel.setText(self.title)
        #
        self.dev = MB110_224()
        self.singleReadPButt.clicked.connect(self.dev.read_temp)
        self.reconnectPButt.clicked.connect(self.dev.reconnect)
        #
        self.update_timer = QtCore.QTimer()
        self.update_timer.timeout.connect(self.update_body)
        self.update_timer.start(500)

    def update_body(self):
        # таблица для отображения температуры
        self.tempTWidget.setRowCount(len(self.dev.data_name))
        for row in range(len(self.dev.data_name)):
            table_item = QtWidgets.QTableWidgetItem(self.dev.data_name[row])
            self.tempTWidget.setItem(row, 0, table_item)
            table_item = QtWidgets.QTableWidgetItem("%.1f" % float(self.dev.data[row]))
            self.tempTWidget.setItem(row, 1, table_item)
        pass
        #
        if self.dev.state == -1:
            self.devNameLabel.setStyleSheet("background-color: " + "lightcoral")
        elif self.dev.state == 1:
            self.devNameLabel.setStyleSheet("background-color: " + "palegreen")


if __name__ == "__main__":
    pass
