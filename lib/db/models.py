from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# City class
class City(Base):
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    country = Column(String, nullable=False)

    weather_stations = relationship("WeatherStation", back_populates="city")
    forecasts = relationship("ForecastData", back_populates="city")
    alert_warnings = relationship("AlertWarning", back_populates="city")
    geographical_infos = relationship("GeographicalInfo", back_populates="city")

    @classmethod
    def add_city(cls, session, name, country):
        session.add(cls(name=name, country=country))
        session.commit()
        print("City added successfully!")

    @classmethod
    def remove_city(cls, session, city_id):
        city = session.query(cls).get(city_id)
        if city:
            session.delete(city)
            session.commit()
            print("City removed successfully!")
        else:
            print("City not found")


# WeatherStation class
class WeatherStation(Base):
    __tablename__ = 'weather_stations'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    city_id = Column(Integer, ForeignKey('cities.id'), nullable=False)

    city = relationship("City", back_populates="weather_stations")
    observations = relationship("Observation", back_populates="weather_station")
    forecasts = relationship("ForecastData", back_populates="weather_station")  

    @classmethod
    def add_station(cls, session, name, city_id):
        session.add(cls(name=name, city_id=city_id))
        session.commit()
        print("Weather station added successfully!")

    @classmethod
    def remove_station(cls, session, station_id):
        station = session.query(cls).get(station_id)
        if station:
            session.delete(station)
            session.commit()
            print("Weather station removed successfully!")
        else:
            print("Weather station not found")

    @classmethod
    def remove_forecast(cls, session, forecast_id):
        forecast = session.query(ForecastData).get(forecast_id)
        if forecast:
            session.delete(forecast)
            session.commit()
            print("Forecast removed successfully!")
        else:
            print("Forecast not found")


# Observation class
class Observation(Base):
    __tablename__ = 'observations'

    id = Column(Integer, primary_key=True)
    temperature = Column(Float, nullable=False)
    humidity = Column(Float, nullable=False)
    timestamp = Column(DateTime, nullable=False)
    weather_station_id = Column(Integer, ForeignKey('weather_stations.id'), nullable=False)

    weather_station = relationship("WeatherStation", back_populates="observations")

    @classmethod
    def add_observation(cls, session, temperature, humidity, timestamp, weather_station_id):
        session.add(cls(temperature=temperature, humidity=humidity, timestamp=timestamp, weather_station_id=weather_station_id))
        session.commit()
        print("Observation added successfully!")

    @classmethod
    def remove_observation(cls, session, observation_id):
        observation = session.query(cls).get(observation_id)
        if observation:
            session.delete(observation)
            session.commit()
            print("Observation removed successfully!")
        else:
            print("Observation not found")


# ForecastData class
class ForecastData(Base):
    __tablename__ = 'forecast_data'

    id = Column(Integer, primary_key=True, index=True)
    weather_station_id = Column(Integer, ForeignKey('weather_stations.id'), nullable=False)
    city_id = Column(Integer, ForeignKey('cities.id'), nullable=False)  
    forecast_date = Column(DateTime, nullable=False)  
    forecast = Column(String(255), nullable=False)  
    forecast_temp = Column(Float, nullable=False)
    forecast_humidity = Column(Float, nullable=False)

    weather_station = relationship("WeatherStation", back_populates="forecasts")  
    city = relationship("City", back_populates="forecasts")  # Corrected here


# AlertWarning class
class AlertWarning(Base):
    __tablename__ = 'alert_warnings'

    id = Column(Integer, primary_key=True)
    message = Column(String, nullable=False)
    alert_type = Column(String, nullable=False)
    city_id = Column(Integer, ForeignKey('cities.id'), nullable=False)

    city = relationship("City", back_populates="alert_warnings")

    @classmethod
    def add_alert(cls, session, message, alert_type, city_id):
        session.add(cls(message=message, alert_type=alert_type, city_id=city_id))
        session.commit()
        print("Alert added successfully!")

    @classmethod
    def remove_alert(cls, session, alert_id):
        alert = session.query(cls).get(alert_id)
        if alert:
            session.delete(alert)
            session.commit()
            print("Alert removed successfully!")
        else:
            print("Alert not found")


# GeographicalInfo class
class GeographicalInfo(Base):
    __tablename__ = 'geographical_info'

    id = Column(Integer, primary_key=True)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    city_id = Column(Integer, ForeignKey('cities.id'), nullable=False)

    city = relationship("City", back_populates="geographical_infos")

    @classmethod
    def add_geographical_info(cls, session, latitude, longitude, city_id):
        session.add(cls(latitude=latitude, longitude=longitude, city_id=city_id))
        session.commit()
        print("Geographical information added successfully!")

    @classmethod
    def remove_geographical_info(cls, session, geo_id):
        geo_info = session.query(cls).get(geo_id)
        if geo_info:
            session.delete(geo_info)
            session.commit()
            print("Geographical information removed successfully!")
        else:
            print("Geographical information not found")
