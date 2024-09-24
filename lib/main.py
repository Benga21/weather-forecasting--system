from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import click
import json
from lib.db.models import City, WeatherStation, Observation, ForecastData, AlertWarning, GeographicalInfo  

DATABASE_URL = "sqlite:///data/weather_data.db"

# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

@click.group()
def cli():
    """A simple CLI application."""
    pass

# Show Data Commands
@click.command()
def show_alert_warnings():
    """Show alert warnings."""
    session = Session()
    alerts = session.query(AlertWarning).all()
    for alert in alerts:
        click.echo(alert)
    session.close()

@click.command()
def show_cities():
    """Show cities."""
    session = Session()
    cities = session.query(City).all()
    for city in cities:
        click.echo(city)
    session.close()

@click.command()
def show_forecast_data():
    """Show forecast data."""
    session = Session()
    forecasts = session.query(ForecastData).all()
    for forecast in forecasts:
        click.echo(forecast)
    session.close()

@click.command()
def show_geographical_info():
    """Show geographical info."""
    session = Session()
    geo_infos = session.query(GeographicalInfo).all()
    for info in geo_infos:
        click.echo(info)
    session.close()

@click.command()
def show_observations():
    """Show observations."""
    session = Session()
    observations = session.query(Observation).all()
    for observation in observations:
        click.echo(observation)
    session.close()

@click.command()
def show_weather_stations():
    """Show weather stations."""
    session = Session()
    stations = session.query(WeatherStation).all()
    for station in stations:
        click.echo(station)
    session.close()

# Add Data Commands
@click.command()
@click.argument('name')
@click.argument('country')
def add_city(name, country):
    """Add a new city."""
    session = Session()
    new_city = City(name=name, country=country)
    session.add(new_city)
    session.commit()
    session.close()
    click.echo("City added successfully.")

@click.command()
@click.argument('city_id')
@click.argument('forecast_data', type=str) 
def add_forecast(city_id, forecast_data):
    """Add a forecast for a city."""
    session = Session()
    forecast_data = json.loads(forecast_data)
    new_forecast = ForecastData(city_id=city_id, **forecast_data)
    session.add(new_forecast)
    session.commit()
    session.close()
    click.echo("Forecast added successfully.")

@click.command()
@click.argument('city_id')
@click.argument('alert_type')
@click.argument('description')
def add_alert_warning(city_id, alert_type, description):
    """Add a new alert warning for a city."""
    session = Session()
    new_alert = AlertWarning(city_id=city_id, alert_type=alert_type, description=description)
    session.add(new_alert)
    session.commit()
    session.close()
    click.echo("Alert warning added successfully.")

@click.command()
@click.argument('geo_info', type=str)
def add_geographical_info(geo_info):
    """Add geographical info."""
    session = Session()
    geo_info = json.loads(geo_info)
    new_geo_info = GeographicalInfo(**geo_info)
    session.add(new_geo_info)
    session.commit()
    session.close()
    click.echo("Geographical info added successfully.")

@click.command()
@click.argument('observation_data', type=str)
def add_observation(observation_data):
    """Add an observation."""
    session = Session()
    observation_data = json.loads(observation_data)
    new_observation = Observation(**observation_data)
    session.add(new_observation)
    session.commit()
    session.close()
    click.echo("Observation added successfully.")

@click.command()
@click.argument('station_data', type=str)
def add_weather_station(station_data):
    """Add a weather station."""
    session = Session()
    station_data = json.loads(station_data)
    new_station = WeatherStation(**station_data)
    session.add(new_station)
    session.commit()
    session.close()
    click.echo("Weather station added successfully.")

# Remove Data Commands
@click.command()
@click.argument('city_id')
def remove_city(city_id):
    """Remove a city by ID."""
    session = Session()
    city = session.query(City).get(city_id)
    if city:
        session.delete(city)
        session.commit()
        click.echo("City removed successfully.")
    else:
        click.echo("City not found.")
    session.close()

@click.command()
@click.argument('forecast_id')
def remove_forecast(forecast_id):
    """Remove a forecast by ID."""
    session = Session()
    forecast = session.query(ForecastData).get(forecast_id)
    if forecast:
        session.delete(forecast)
        session.commit()
        click.echo("Forecast removed successfully.")
    else:
        click.echo("Forecast not found.")
    session.close()

@click.command()
@click.argument('alert_id')
def remove_alert_warning(alert_id):
    """Remove an alert warning by ID."""
    session = Session()
    alert = session.query(AlertWarning).get(alert_id)
    if alert:
        session.delete(alert)
        session.commit()
        click.echo("Alert warning removed successfully.")
    else:
        click.echo("Alert warning not found.")
    session.close()

@click.command()
@click.argument('geo_info_id')
def remove_geographical_info(geo_info_id):
    """Remove geographical info by ID."""
    session = Session()
    geo_info = session.query(GeographicalInfo).get(geo_info_id)
    if geo_info:
        session.delete(geo_info)
        session.commit()
        click.echo("Geographical info removed successfully.")
    else:
        click.echo("Geographical info not found.")
    session.close()

@click.command()
@click.argument('observation_id')
def remove_observation(observation_id):
    """Remove an observation by ID."""
    session = Session()
    observation = session.query(Observation).get(observation_id)
    if observation:
        session.delete(observation)
        session.commit()
        click.echo("Observation removed successfully.")
    else:
        click.echo("Observation not found.")
    session.close()

@click.command()
@click.argument('station_id')
def remove_weather_station(station_id):
    """Remove a weather station by ID."""
    session = Session()
    station = session.query(WeatherStation).get(station_id)
    if station:
        session.delete(station)
        session.commit()
        click.echo("Weather station removed successfully.")
    else:
        click.echo("Weather station not found.")
    session.close()

# Add commands to the CLI group
cli.add_command(show_alert_warnings)
cli.add_command(show_cities)
cli.add_command(show_forecast_data)
cli.add_command(show_geographical_info)
cli.add_command(show_observations)
cli.add_command(show_weather_stations)
cli.add_command(add_city)
cli.add_command(add_forecast)
cli.add_command(add_alert_warning)
cli.add_command(add_geographical_info)
cli.add_command(add_observation)
cli.add_command(add_weather_station)
cli.add_command(remove_city)
cli.add_command(remove_forecast)
cli.add_command(remove_alert_warning)
cli.add_command(remove_geographical_info)
cli.add_command(remove_observation)
cli.add_command(remove_weather_station)

if __name__ == '__main__':
    cli()
