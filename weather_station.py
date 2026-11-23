class Subject:
    def registerObserver(self, observer):
        pass

    def removeObserver(self, observer):
        pass

    def notifyObservers(self):
        pass

class Observer:
    def update(self, temp, humidity, pressure):
        pass

# WeatherData now implements the subject interface.
class WeatherData(Subject):
    
    def __init__(self):        
        self.observers = []
        self.temperature = 0
        self.humidity = 0
        self.pressure = 0
    
    
    def registerObserver(self, observer):
        # When an observer registers, we just 
        # add it to the end of the list.
        self.observers.append(observer)
        
    def removeObserver(self, observer):
        if observer not in self.observers:
            return
        self.observers.remove(observer)
    
    def notifyObservers(self):
        for ob in self.observers:
            ob.update(
                self.getTemperature(),
                self.getHumidity(),
                self.getPressure(),
            )

    def measurementsChanged(self):
        self.notifyObservers()

    def setMeasurements(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.measurementsChanged()

    def getTemperature(self):
        return self.temperature

    def getHumidity(self):
        return self.humidity

    def getPressure(self):
        return self.pressure

class Display(Observer):

    def __init__(self, weatherData):
        self.temperature = 0
        self.humidity = 0
        self.pressure = 0
        self.weatherData = weatherData
        weatherData.registerObserver(self)

    def update(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.display()

    def display(self):
        pass

class CurrentConditionsDisplay(Display):

    def display(self):
        print(
            "Current conditions:",
            self.temperature, "F degrees and",
            self.humidity, "[%] humidity",
            "and pressure", self.pressure,
        )

class ForecastDisplay(Display):

    def forecast_temp(self):
        return self.temperature + 0.11 * self.humidity + 0.2 * self.pressure

    def forecast_humidity(self):
        return self.humidity - 0.9 * self.humidity

    def forecast_pressure(self):
        return self.pressure + 0.1 * self.temperature - 0.21 * self.pressure

    def display(self):
        print(
            "Forecast:",
            self.forecast_temp(), "F,",
            self.forecast_humidity(), "[%] humidity,",
            "pressure", self.forecast_pressure(),
        )

class StatisticsDisplay(Display):

    def __init__(self, weatherData):
        self.temps = []
        super().__init__(weatherData)

    def update(self, temperature, humidity, pressure):
        self.temps.append(temperature)
        super().update(temperature, humidity, pressure)

    def min_temp(self):
        return min(self.temps)

    def max_temp(self):
        return max(self.temps)

    def avg_temp(self):
        return sum(self.temps) / len(self.temps)

    def display(self):
        if not self.temps:
            return
        print(
            "Avg/Max/Min temperature:",
            self.avg_temp(), "/",
            self.max_temp(), "/",
            self.min_temp(),
        )

class WeatherStation:
    def main(self):
        weather_data = WeatherData()
        current_display = CurrentConditionsDisplay(weather_data)
        stats_display = StatisticsDisplay(weather_data)
        forecast_display = ForecastDisplay(weather_data)

        weather_data.setMeasurements(80, 65, 30.4)
        weather_data.setMeasurements(82, 70, 29.2)
        weather_data.setMeasurements(78, 90, 29.2)

        weather_data.removeObserver(current_display)
        weather_data.setMeasurements(120, 100, 1000)


if __name__ == "__main__":
    w = WeatherStation()
    w.main()
