class Subject:
    # Both of the following two methods take an
    # observer as an argument; that is, the observer
    # to be registered ore removed.
    def registerObserver(observer):
        pass
    def removeObserver(observer):
        pass
    
    # This method is called to notify all observers
    # when the Subject's state (measuremetns) has changed.
    def notifyObservers():
        pass
    
# The observer class is implemented by all observers,
# so they all have to implemented the update() method. Here
# we're following Mary and Sue's lead and 
# passing the measurements to the observers.
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

    def display(self):
        forecast_temp = self.temperature + 0.11 * self.humidity + 0.2 * self.pressure
        forecast_humidity = self.humidity - 0.9 * self.humidity
        forecast_pressure = self.pressure + 0.1 * self.temperature - 0.21 * self.pressure
        print(
            "Forecast:",
            forecast_temp, "F,",
            forecast_humidity, "[%] humidity,",
            "pressure", forecast_pressure,
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
        
        # TODO: Create two objects from StatisticsDisplay class and 
        # ForecastDisplay class. Also register them to the concerete instance
        # of the Subject class so the they get the measurements' updates.
        
        # The StatisticsDisplay class should keep track of the min/average/max
        # measurements and display them.
        
        # The ForecastDisplay class shows the weather forcast based on the current
        # temperature, humidity and pressure. Use the following formuals :
        # forcast_temp = temperature + 0.11 * humidity + 0.2 * pressure
        # forcast_humadity = humidity - 0.9 * humidity
        # forcast_pressure = pressure + 0.1 * temperature - 0.21 * pressure
        
        weather_data.setMeasurements(80, 65,30.4)
        weather_data.setMeasurements(82, 70,29.2)
        weather_data.setMeasurements(78, 90,29.2)
        
        # un-register the observer
        weather_data.removeObserver(current_display)
        weather_data.setMeasurements(120, 100,1000)
    
        

if __name__ == "__main__":
    w = WeatherStation()
    w.main()