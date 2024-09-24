from sqlalchemy.orm import Session
from lib.db.database import SessionLocal
from lib.db.models import City, WeatherStation, Observation, ForecastData, AlertWarning, GeographicalInfo
def add_data():
    db: Session = SessionLocal()
    try:
        print("Adding sample cities...")
        cities = [
            City(name="New York 🌆", country="USA"),
            City(name="Los Angeles 🌴", country="USA"),
            # Add more cities as needed
        ]
        db.add_all(cities)
        db.commit()
        print("Cities added successfully!")

        print("Adding sample weather stations...")
        stations = [
            WeatherStation(name="Central Park Station", city_id=1),  
            WeatherStation(name="Hollywood Station", city_id=2),
            
        ]
        db.add_all(stations)
        db.commit()
        print("Weather stations added successfully!")

        print("Adding sample observations...")
        observations = [
            Observation(station_id=1, temperature=25.0, humidity=60),
            Observation(station_id=2, temperature=28.0, humidity=55),
            
        ]
        db.add_all(observations)
        db.commit()
        print("Observations added successfully!")

        print("Adding sample forecast data...")
        forecasts = [
            ForecastData(station_id=1, forecast_temp=27.0, forecast_humidity=65),  
            ForecastData(station_id=2, forecast_temp=29.0, forecast_humidity=50),
            
        ]
        db.add_all(forecasts)
        db.commit()
        print("Forecast data added successfully!")

        print("Adding sample alerts...")
        alerts = [
            AlertWarning(station_id=1, alert_type="Severe Thunderstorm", description="Severe thunderstorm warning issued."),
            AlertWarning(station_id=2, alert_type="Heat Advisory", description="Heat advisory in effect."),
            # Add more alerts as needed
        ]
        db.add_all(alerts)
        db.commit()
        print("Alerts added successfully!")

        print("Adding sample geographical info...")
        geo_info = [
            GeographicalInfo(station_id=1, latitude=40.785091, longitude=-73.968285),  
            GeographicalInfo(station_id=2, latitude=34.052235, longitude=-118.243683),  
            
        ]
        db.add_all(geo_info)
        db.commit()
        print("Geographical information added successfully!")

    except Exception as e:
        db.rollback()
        print(f"An error occurred: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    add_data()
