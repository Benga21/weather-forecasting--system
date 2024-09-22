from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from .database import Base

class City(Base):
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    country = Column(String, nullable=False)

    weather_stations = relationship("WeatherStation", back_populates="city")
    alerts = relationship("AlertWarning", back_populates="city")
    geographical_info = relationship("GeographicalInfo", back_populates="city")


class WeatherStation(Base):
    __tablename__ = 'weather_stations'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    city_id = Column(Integer, ForeignKey('cities.id'), nullable=False)

    city = relationship("City", back_populates="weather_stations")
    observations = relationship("Observation", back_populates="weather_station")
    forecasts = relationship("ForecastData", back_populates="weather_station")


class Observation(Base):
    __tablename__ = 'observations'

    id = Column(Integer, primary_key=True)
    temperature = Column(Float, nullable=False)
    humidity = Column(Float, nullable=False)
    timestamp = Column(DateTime, nullable=False)
    weather_station_id = Column(Integer, ForeignKey('weather_stations.id'), nullable=False)

    weather_station = relationship("WeatherStation", back_populates="observations")


class ForecastData(Base):
    __tablename__ = 'forecast_data'

    id = Column(Integer, primary_key=True, index=True)
    weather_station_id = Column(Integer, ForeignKey('weather_stations.id'))
    forecast = Column(String, nullable=False)
    forecast_temp = Column(Float, nullable=False)
    forecast_humidity = Column(Float, nullable=False)

    weather_station = relationship("WeatherStation", back_populates="forecasts")


class AlertWarning(Base):
    __tablename__ = 'alert_warnings'

    id = Column(Integer, primary_key=True)
    alert_type = Column(String, nullable=False)
    message = Column(String, nullable=False)
    city_id = Column(Integer, ForeignKey('cities.id'), nullable=False)

    city = relationship("City", back_populates="alerts")


class GeographicalInfo(Base):
    __tablename__ = 'geographical_info'

    id = Column(Integer, primary_key=True)
    city_id = Column(Integer, ForeignKey('cities.id'), nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)

    city = relationship("City", back_populates="geographical_info")
