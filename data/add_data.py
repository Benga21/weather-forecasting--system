import logging
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from lib.db.models import City, WeatherStation, Observation, Forecast, AlertWarning, GeographicalInfo
from datetime import datetime

DATABASE_URL = "sqlite:///data/weather_data.db"

def add_data():
    logging.basicConfig(level=logging.INFO)
    engine = create_engine(DATABASE_URL)
    Session = sessionmaker(bind=engine)

    session = Session()

    # Cities
    cities = [
        City(name="New York 🌆", country="USA"),
        City(name="Tokyo 🗼", country="Japan"),
        City(name="Paris 🇫🇷", country="France"),
        City(name="Sydney 🦘", country="Australia"),
        City(name="Cairo 🏺", country="Egypt"),
        City(name="Rio de Janeiro 🌴", country="Brazil"),
    ]
    session.add_all(cities)
    session.commit()
    logging.info("Cities added successfully.")
    
    # Weather Stations
    stations = [
        WeatherStation(name="Central Park Station", city=cities[0]),
        WeatherStation(name="Tokyo Tower Station", city=cities[1]),
        WeatherStation(name="Eiffel Tower Station", city=cities[2]),
        WeatherStation(name="Sydney Opera House Station", city=cities[3]),
        WeatherStation(name="Giza Pyramids Station", city=cities[4]),
        WeatherStation(name="Copacabana Station", city=cities[5]),
    ]
    session.add_all(stations)
    session.commit()
    logging.info("Weather stations added successfully.")
    
    # Observations
    observations = [
        Observation(temperature=60.0, humidity=60.0, timestamp=datetime(2024, 9, 19, 6, 0), weather_station=stations[0]),
        Observation(temperature=50.0, humidity=70.0, timestamp=datetime(2024, 9, 19, 6, 0), weather_station=stations[1]),
        Observation(temperature=40.0, humidity=50.0, timestamp=datetime(2024, 9, 19, 6, 0), weather_station=stations[2]),
        Observation(temperature=32.0, humidity=65.0, timestamp=datetime(2024, 9, 19, 6, 0), weather_station=stations[3]),
        Observation(temperature=20.0, humidity=80.0, timestamp=datetime(2024, 9, 19, 6, 0), weather_station=stations[4]),
        Observation(temperature=26.0, humidity=75.0, timestamp=datetime(2024, 9, 19, 6, 0), weather_station=stations[5]),
    ]
    session.add_all(observations)
    session.commit()
    logging.info("Observations added successfully.")
    
    # Forecasts
    forecasts = [
        Forecast(city_id=cities[0].id, temperature=75.0, description="Sunny ☀️", date=datetime(2024, 9, 20)),
    Forecast(city_id=cities[1].id, temperature=60.0, description="Rainy 🌧️", date=datetime(2024, 9, 20)),
    Forecast(city_id=cities[2].id, temperature=65.0, description="Cloudy ☁️", date=datetime(2024, 9, 20)),
    Forecast(city_id=cities[3].id, temperature=70.0, description="Windy 🌬️", date=datetime(2024, 9, 20)),
    Forecast(city_id=cities[4].id, temperature=90.0, description="Hot 🔥", date=datetime(2024, 9, 20)),
    Forecast(city_id=cities[5].id, temperature=50.0, description="Cold ❄️", date=datetime(2024, 9, 20)),
    ]
    session.add_all(forecasts)
    session.commit()
    logging.info("Forecast data added successfully.")
    
    # Alert Warnings
    alerts = [
        AlertWarning(message="Extreme heat expected in New York.", alert_type="Heatwave 🔥", city_id=cities[0].id),
    AlertWarning(message="Typhoon approaching Tokyo.", alert_type="Typhoon 🌪️", city_id=cities[1].id),
    AlertWarning(message="Heavy rain expected in Paris.", alert_type="Flood Warning 🌊", city_id=cities[2].id),
    AlertWarning(message="High fire risk in Sydney.", alert_type="Wildfire 🔥", city_id=cities[3].id),
    AlertWarning(message="Sandstorm warning in Cairo.", alert_type="Sandstorm 🌫️", city_id=cities[4].id),
    AlertWarning(message="Tsunami alert for Rio de Janeiro.", alert_type="Tsunami 🌊", city_id=cities[5].id),
]
    session.add_all(alerts)
    session.commit()
    logging.info("Alert warnings added successfully.")
    
    # Geographical Info
    geo_info = [
        GeographicalInfo(city_id=cities[0].id, latitude=40.7128, longitude=-74.0060),
        GeographicalInfo(city_id=cities[1].id, latitude=35.6762, longitude=139.6503),
        GeographicalInfo(city_id=cities[2].id, latitude=48.8566, longitude=2.3522),
        GeographicalInfo(city_id=cities[3].id, latitude=-33.8688, longitude=151.2093),
        GeographicalInfo(city_id=cities[4].id, latitude=30.0444, longitude=31.2357),
        GeographicalInfo(city_id=cities[5].id, latitude=-22.9068, longitude=-43.1729),
    ]
    session.add_all(geo_info)
    session.commit()
    logging.info("Geographical information added successfully.")

    session.close()
    logging.info("Data population completed.")

if __name__ == "__main__":
    add_data()
