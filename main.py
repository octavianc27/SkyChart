import PyQt5
import astronomy
import math
import matplotlib
import matplotlib.pyplot as plt
import sys
from geopy.geocoders import Nominatim
from hipparcos import querryHip
from layout import Ui_MainWindow
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as Canvas
from matplotlib.figure import Figure

# tre ca sa mearga
matplotlib.use('QT5Agg')

# aspect plot
plt.style.use("classic")

# apiul pt geolocatie
geolocate = Nominatim(user_agent="StarChart")

app = PyQt5.QtWidgets.QApplication(sys.argv)
MainWindow = PyQt5.QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)

location = Null


# widgetul pt grafic


class MyMplCanvas(Canvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)

        self.axes = fig.add_subplot(111, projection='polar')

        Canvas.__init__(self, fig)
        self.setParent(parent)

        self.update_figure()

        Canvas.setSizePolicy(self,
                             PyQt5.QtWidgets.QSizePolicy.Expanding,
                             PyQt5.QtWidgets.QSizePolicy.Expanding)
        Canvas.updateGeometry(self)

    def compute_initial_figure(self):
        pass


class StarChart(MyMplCanvas):
    def __init__(self, *args, **kwargs):
        MyMplCanvas.__init__(self, *args, **kwargs)

    def update_figure(self):
        self.axes.cla()

        self.axes.set_theta_zero_location("N")
        self.axes.set_theta_direction(-1)
        self.axes.set_xticklabels(['N', '', 'W', '', 'S', '', 'E', ''])
        self.axes.set_ylim(0, 90)
        self.axes.set_yticklabels([])

        alt, az, mag = astronomy.get_coords(ui.locatie_selectata.text(), ui.dateTimeEdit.dateTime().toPyDateTime())
        # print(len(alt), len(az), len(mag))
        self.axes.scatter(az * 2 * math.pi / 360, alt, s=mag, color='black')
        self.draw()


chartWidget = PyQt5.QtWidgets.QVBoxLayout(ui.map_display)
sc = StarChart(ui.map_display, width=5, height=4, dpi=100)
chartWidget.addWidget(sc)


# button handling functions


def reset():
    ui.dateTimeEdit.setDateTime(PyQt5.QtCore.QDateTime.currentDateTime())
    ui.edit_locatie.setText("Sibiu")
    update_location()


def update():
    sc.update_figure()


def update_location():
    global location
    location = geolocate.geocode(ui.edit_locatie.text().lower()).raw
    ui.locatie_selectata.setText(location["display_name"])
    update()


def plus24h():
    ui.dateTimeEdit.setDateTime(ui.dateTimeEdit.dateTime().addDays(1))
    update()


def minus24h():
    ui.dateTimeEdit.setDateTime(ui.dateTimeEdit.dateTime().addDays(-1))
    update()


def plus1h():
    ui.dateTimeEdit.setDateTime(ui.dateTimeEdit.dateTime().addSecs(3600))
    update()


def minus1h():
    ui.dateTimeEdit.setDateTime(ui.dateTimeEdit.dateTime().addSecs(-3600))
    update()


querryHip()
reset()

# button handler connections
ui.button_update.clicked.connect(update_location)
ui.button_plus24h.clicked.connect(plus24h)
ui.button_minus24h.clicked.connect(minus24h)
ui.button_plus1h.clicked.connect(plus1h)
ui.button_minus1h.clicked.connect(minus1h)
ui.buton_reset.clicked.connect(reset)

MainWindow.show()
sys.exit(app.exec_())
