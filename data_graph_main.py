# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QMainWindow, QTableWidgetItem
import data_graph

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt


class MainWindow(QMainWindow, data_graph.Ui_GraphWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.type = "slave"  # необходимо для проерки на вид вызова окна - главное/дочернее
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self)
        # data
        self.data = None
        self.pause = 0
        self.graph_point_num = 3600
        # set the layout
        layout = QVBoxLayout()
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)
        self.graphicsViews.setLayout(layout)
        #
        self.pauseButton.toggled.connect(self.pause_set_clr)

    def pause_set_clr(self, checked):
        if checked:
            self.pause = 1
        else:
            self.pause = 0

    def plot(self, data=None):
        self.graph_point_num = self.pointNumSBox.value()
        try:
            if self.pause == 0:
                self.data = data
                try:
                    time = self.data[0][1][-self.graph_point_num:]
                    data_y = [self.data[i][1][-self.graph_point_num:] for i in range(1, len(self.data))]
                except IndexError:
                    time = self.data[0][1]
                    data_y = [self.data[i][1] for i in range(1, len(self.data))]
                names = [self.data[i][0] for i in range(1, len(self.data))]
                # отрисуем график
                # instead of ax.hold(False)
                self.figure.clear()
                # create an axis
                # axes = self.figure.add_subplot(111)
                axes = self.figure.add_axes([0.1, 0.1, 0.85, 0.90])
                # plot data
                [axes.plot(time, data_y[i], line_type_from_index(i), label=names[i]) for i in range(len(data_y))]
                axes.legend(loc='best', bbox_to_anchor=(0.1, 0.1, 0.5, 0.8))
                # axes.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
                axes.set_xlabel("Время, с")
                axes.grid()
                # refresh canvas
                self.canvas.draw()
                # заполним таблицу
                self.tableWidget.setRowCount(len(self.data) + 1)
                time_name_item = QTableWidgetItem("Время")
                self.tableWidget.setItem(0, 1, time_name_item)
                time_item = QTableWidgetItem("NA")  # "{:.3g}".format(data_x[0][-1]))
                self.tableWidget.setItem(0, 2, time_item)
                for row in range(len(names)):
                    for column in range(0, 2):
                        if column == 0:
                            table_item = QTableWidgetItem(names[row])
                        elif column == 1:
                            try:
                                table_item = QTableWidgetItem("{:.3g}".format(data_y[row][-1]))
                            except IndexError:
                                table_item = QTableWidgetItem("NA")
                        else:
                            table_item = QTableWidgetItem("NA")
                        self.tableWidget.setItem(row, column, table_item)
            else:
                pass
        except Exception as error:
            print(error)

    # Переопределение метода closeEvent, для перехвата события закрытия окна
    def closeEvent(self, event):
        if self.type == "master":
            event.ignore()
        else:
            self.hide()


def line_type_from_index(n):
    color_line = ["b", "r", "g", "c", "m", "y", "k"]
    style_line = ["-", "--", "-.", ":"]
    try:
        color = color_line[n % len(color_line)]
        style = style_line[n // len(color_line)]
        # print(n % len(color_line), n // len(color_line))
        return style + color
    except Exception:
        return "-r"


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MainWindow()
    main.type = "master"
    main.show()
    sys.exit(app.exec_())
