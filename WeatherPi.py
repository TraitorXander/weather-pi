import sys, time, requests, json, Common, apikey, threading, datetime
from datetime import timedelta

from PyQt5 import QtWidgets, uic
from timeloop import Timeloop

city = apikey.location
api_key = apikey.key
api_url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(
    city, api_key)

tl = Timeloop()
window = None
response = requests.get(api_url)
timeNow = time.time()


@tl.job(interval=timedelta(seconds=1))
def UpdateTime():
    print("Time call...")
    window.lblDate.setText(str(datetime.datetime.now()))


@tl.job(interval=timedelta(seconds=3600))
def UpdateGUI():
    print("Job call...")
    window.lblLocation.setText(
        str(response.json()['name']) + ", " +
        str(response.json()['sys']['country'])
    )

    window.lblCurrWeather.setText(
        "Temp: " + str(response.json()['main']['temp']) + u"\N{DEGREE SIGN}C" +
        "\nFeels like: " + str(response.json()['main']['feels_like'])+ u"\N{DEGREE SIGN}C" +
        "\nFeels like: " + str(response.json()['main']['feels_like'])+ u"\N{DEGREE SIGN}C" +
        "\nMin: " + str(response.json()['main']['temp_min'])+ u"\N{DEGREE SIGN}C" +
        "Max: " + str(response.json()['main']['temp_max'])+ u"\N{DEGREE SIGN}C"
    )


def InitAPI(self):
    print(api_url)
    response = requests.get(api_url)

    # If the response code is good
    print("API Response Code: " + Common.GetResponseCode(response.status_code))
    if (response.status_code == 200):
        #print(response.json())
        UpdateGUI()
        tl.start(block=False)
    else:
        self.lblLocation.setText("API Error: " + Common.GetResponseCode(response.status_code))
        tl.start(block=False)
        return

class WeatherPi(QtWidgets.QMainWindow):
    def __init__(self):
        super(WeatherPi,
              self).__init__()  # Call the inherited classes __init__ method
        uic.loadUi('frmMain.ui', self)  # Load the .ui file
        self.show()  # Show the GUI
        self.setStyleSheet("background-color: #d3d3d3;")
        InitAPI(self)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = WeatherPi()
    app.exec_()
