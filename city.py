import pprint
import requests


class OpenWeatherForecast:


    def get(self, city):
        url = f'https://samples.openweathermap.org/data/2.5/forecast/hourly?id=501175&appid=439d4b804bc8187953eb36d2a8c26a02'
        data = requests(url).json()
        forecast_data = data["list"]
        forecast = []
        for h, hour_data in enumerate(forecast_data):
            forecast.append({
                "hour": hour_data[]
            })


class CityInfo:

    def __init__(self, City):
        self.city = city

    def weather_forecast(self):
        pass


def _main():
    city_info = CityInfo("Moskow")
    forecast = city_info.weather_forecast()
    pptint.pprint(forecast)

if __name__ == "__main__":
    _main