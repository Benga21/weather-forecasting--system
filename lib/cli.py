import click
from prettytable import PrettyTable
from lib.db.database import SessionLocal
from lib.db.models import City, WeatherStation, Observation, ForecastData, AlertWarning, GeographicalInfo


@click.group()
def cli():
    """Weather Forecast CLI"""
    pass

@cli.command()
def show_cities():
    """Show cities data"""
    db = SessionLocal()
    cities = db.query(City).all()
    print_table("Cities", cities, ["id", "name", "country"])
    db.close()

@cli.command()
def show_weather_stations():
    """Show weather stations data"""
    db = SessionLocal()
    stations = db.query(WeatherStation).all()
    print_table("Weather Stations", stations, ["id", "name", "location"])
    db.close()

@cli.command()
def show_observations():
    """Show observations data"""
    db = SessionLocal()
    observations = db.query(Observation).all()
    print_table("Observations", observations, ["id", "temperature", "humidity", "timestamp", "city_id", "weather_station_id"])
    db.close()

@cli.command()
def show_forecast_data():
    """Show forecast data"""
    db = SessionLocal()
    forecasts = db.query(ForecastData).all()
    print_table("Forecast Data", forecasts, ["id", "city_id", "forecast"])
    db.close()

@cli.command()
def show_alert_warnings():
    """Show alert warnings data"""
    db = SessionLocal()
    alerts = db.query(AlertWarning).all()
    print_table("Alert Warnings", alerts, ["id", "alert_type", "message", "city_id"])
    db.close()

@cli.command()
def show_geographical_info():
    """Show geographical info data"""
    db = SessionLocal()
    geography = db.query(GeographicalInfo).all()
    print_table("Geographical Info", geography, ["id", "city_id", "latitude", "longitude"])
    db.close()

def print_table(title, data, columns):
    """Helper function to print data in a PrettyTable format"""
    table = PrettyTable()
    table.field_names = columns
    for item in data:
        table.add_row([getattr(item, col, '') for col in columns])
    print(f"\n{title}:\n{table}")

if __name__ == "__main__":
    cli()
