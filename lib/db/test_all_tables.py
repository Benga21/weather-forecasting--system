import pytest
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from lib.db.models import Base, City, WeatherStation, ForecastData, Observation, AlertWarning, GeographicalInfo  


DATABASE_URL = "sqlite:///:memory:"

@pytest.fixture(scope='function')
def test_session():
    engine = create_engine(DATABASE_URL, echo=False)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.close()
    Base.metadata.drop_all(engine)

@pytest.fixture
def example_city(test_session):
    city = City(name="San Francisco", country="USA")
    test_session.add(city)
    test_session.commit()
    return city

@pytest.fixture
def example_station(test_session, example_city):
    station = WeatherStation(name="Central Park Station", city_id=example_city.id)
    test_session.add(station)
    test_session.commit()
    return station

@pytest.fixture
def example_forecast(test_session, example_station, example_city):
    forecast = ForecastData(
        weather_station_id=example_station.id,
        city_id=example_city.id,
        forecast_date=datetime.utcnow(),  # Ensure forecast_date is set
        forecast="Sunny",
        forecast_temp=25.0,
        forecast_humidity=50.0
    )
    test_session.add(forecast)
    test_session.commit()
    return forecast

def test_insert_weather_station(test_session, example_city):
    new_station = WeatherStation(name="Downtown Station", city_id=example_city.id)
    test_session.add(new_station)
    test_session.commit()

    stations = test_session.query(WeatherStation).filter_by(name="Downtown Station").all()
    assert len(stations) == 1, "Weather station was not added successfully."
    assert stations[0].city_id == example_city.id, "Weather station's city_id is incorrect."

def test_insert_observation(test_session, example_station):
    new_observation = Observation(
        weather_station_id=example_station.id,
        temperature=20.5,
        humidity=60.0,
        timestamp=datetime(2024, 9, 19, 6, 0)
    )
    test_session.add(new_observation)
    test_session.commit()

    observations = test_session.query(Observation).filter_by(weather_station_id=example_station.id).all()
    assert len(observations) == 1, "Observation was not added successfully."
    assert observations[0].temperature == 20.5, "Temperature was not stored correctly."

def test_insert_forecast(test_session, example_station, example_city, example_forecast):
    new_forecast = ForecastData(
        weather_station_id=example_station.id,
        city_id=example_city.id,
        forecast_date=datetime.utcnow(),  # Ensure forecast_date is set
        forecast="Rainy",
        forecast_temp=18.0,
        forecast_humidity=80.0
    )
    test_session.add(new_forecast)
    test_session.commit()

    forecasts = test_session.query(ForecastData).filter_by(weather_station_id=example_station.id).all()
    assert len(forecasts) == 2, "Forecast was not added successfully."  
    assert forecasts[-1].forecast == "Rainy", "Forecast type was not stored correctly."
    assert forecasts[-1].forecast_temp == 18.0, "Forecast temperature was not stored correctly."

def test_insert_alert(test_session, example_city):
    new_alert = AlertWarning(
        alert_type="Storm",
        message="Heavy rain expected",
        city_id=example_city.id
    )
    test_session.add(new_alert)
    test_session.commit()

    alerts = test_session.query(AlertWarning).filter_by(city_id=example_city.id).all()
    assert len(alerts) == 1, "Alert was not added successfully."
    assert alerts[0].alert_type == "Storm", "Alert type was not stored correctly."

def test_insert_geographical_info(test_session, example_city):
    new_geo_info = GeographicalInfo(
        city_id=example_city.id,
        latitude=37.7749,
        longitude=-122.4194
    )
    test_session.add(new_geo_info)
    test_session.commit()

    geo_info = test_session.query(GeographicalInfo).filter_by(city_id=example_city.id).all()
    assert len(geo_info) == 1, "Geographical information was not added successfully."
    assert geo_info[0].latitude == 37.7749, "Latitude was not stored correctly."
    assert geo_info[0].longitude == -122.4194, "Longitude was not stored correctly."

if __name__ == "__main__":
    pytest.main()