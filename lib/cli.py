import click 
from prettytable import PrettyTable
from lib.db.database import SessionLocal
from lib.db.models import City, WeatherStation, Observation, ForecastData, AlertWarning, GeographicalInfo


@click.group()
def cli():
    """Weather Forecast CLI"""
    pass

def show_data(model, title, columns):
    """Helper function to show data"""
    with SessionLocal() as db:
        data = db.query(model).all()
        print_table(title, data, columns)

def add_data(model, **kwargs):
    """Helper function to add data"""
    with SessionLocal() as db:
        new_entry = model(**kwargs)
        db.add(new_entry)
        db.commit()
        click.echo(f"{model.__name__} added successfully.")

def remove_data_by_name(model, name):
    """Helper function to remove data by name"""
    with SessionLocal() as db:
        entry = db.query(model).filter(model.name == name).first()  
        if entry:
            db.delete(entry)
            db.commit()
            click.echo(f"{model.__name__} '{name}' removed successfully.")
        else:
            click.echo(f"{model.__name__} '{name}' not found.")

# Show data commands
@cli.command()
def show_cities():
    show_data(City, "Cities", ["id", "name", "country"])

@cli.command()
def show_weather_stations():
    show_data(WeatherStation, "Weather Stations", ["id", "name", "location"])

@cli.command()
def show_observations():
    show_data(Observation, "Observations", ["id", "temperature", "humidity", "timestamp", "weather_station_id"])

@cli.command()
def show_forecast_data():
    show_data(ForecastData, "Forecast Data", ["id", "city_id", "forecast"])

@cli.command()
def show_alert_warnings():
    show_data(AlertWarning, "Alert Warnings", ["id", "alert_type", "message", "city_id"])

@cli.command()
def show_geographical_info():
    show_data(GeographicalInfo, "Geographical Info", ["id", "city_id", "latitude", "longitude"])

# Add data commands
@cli.command()
@click.argument('name')
@click.argument('country')
def add_city(name, country):
    add_data(City, name=name, country=country)

@cli.command()
@click.argument('name')
@click.argument('location')
def add_weather_station(name, location):
    add_data(WeatherStation, name=name, location=location)

@cli.command()
@click.argument('temperature')
@click.argument('humidity')
@click.argument('timestamp')
@click.argument('weather_station_id')
def add_observation(temperature, humidity, timestamp, weather_station_id):
    add_data(Observation, temperature=temperature, humidity=humidity, timestamp=timestamp, weather_station_id=weather_station_id)

@cli.command()
@click.argument('city_id')
@click.argument('forecast')
def add_forecast(city_id, forecast):
    add_data(ForecastData, city_id=city_id, forecast=forecast)

@cli.command()
@click.argument('alert_type')
@click.argument('message')
@click.argument('city_id')
def add_alert_warning(alert_type, message, city_id):
    add_data(AlertWarning, alert_type=alert_type, message=message, city_id=city_id)

@cli.command()
@click.argument('city_id')
@click.argument('latitude')
@click.argument('longitude')
def add_geographical_info(city_id, latitude, longitude):
    add_data(GeographicalInfo, city_id=city_id, latitude=latitude, longitude=longitude)

# Remove data commands
@cli.command()
@click.argument('name')
def remove_city(name):
    remove_data_by_name(City, name)

@cli.command()
@click.argument('name')
def remove_weather_station(name):
    remove_data_by_name(WeatherStation, name)

@cli.command()
@click.argument('id')  
def remove_observation(id):
    with SessionLocal() as db:
        entry = db.query(Observation).get(id)
        if entry:
            db.delete(entry)
            db.commit()
            click.echo(f"Observation with ID '{id}' removed successfully.")
        else:
            click.echo(f"Observation with ID '{id}' not found.")

@cli.command()
@click.argument('id')  
def remove_forecast(id):
    with SessionLocal() as db:
        entry = db.query(ForecastData).get(id)
        if entry:
            db.delete(entry)
            db.commit()
            click.echo(f"ForecastData with ID '{id}' removed successfully.")
        else:
            click.echo(f"ForecastData with ID '{id}' not found.")

@cli.command()
@click.argument('name')
def remove_alert_warning(name):
    remove_data_by_name(AlertWarning, name)

@cli.command()
@click.argument('id')  
def remove_geographical_info(id):
    with SessionLocal() as db:
        entry = db.query(GeographicalInfo).get(id)
        if entry:
            db.delete(entry)
            db.commit()
            click.echo(f"GeographicalInfo with ID '{id}' removed successfully.")
        else:
            click.echo(f"GeographicalInfo with ID '{id}' not found.")

def print_table(title, data, columns):
    """Helper function to print data in a PrettyTable format"""
    table = PrettyTable()
    table.field_names = columns
    for item in data:
        table.add_row([getattr(item, col, '') for col in columns])
    print(f"\n{title}:\n{table}")

if __name__ == "__main__":
    cli()
