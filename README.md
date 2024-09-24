# Phase 3 Project: Weather Forecast CLI Application

## Overview

For this phase 3 project, i create a CLI and ORM application in Python. python 

- Developing a CLI application that addresses a real-world problem while adhering to best practices.
- Creating and modifying a database with SQLAlchemy ORM, including 6 related tables.
- Maintaining a well-structured virtual environment using Pipenv.
- Organizing  application with a proper package structure.
- Utilizing lists, dictionaries, and tuples effectively.

## Features

- Show weather stations data
- Show forecast data
- Show alert warnings data

## Requirements

- Python
- Pipenv (for managing the virtual environment)
- SQLite (for the database)

## Setup Instructions

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/weather_forecast_system.git
   cd weather_forecast_system
Set Up a Virtual Environment Using Pipenv

bash
Copy code
pip install pipenv
Then, create and activate the virtual environment:

bash
Copy code
pipenv install
pipenv shell
Install Dependencies

install the necessary dependencies.  run:

bash
Copy code
pipenv install
Set Up the Database

To set up the database, run:

bash
Copy code
python data/setup_database.py
Run Migrations

Alembic for migrations, run:

bash
Copy code
alembic upgrade head
Usage
You can run the CLI to interact with the system:

bash
Copy code
python lib/cli.py --help
Example Commands
Show weather stations data:

bash
Copy code
python lib/cli.py show-weather-stations
Show forecast data:

bash
Copy code
python lib/cli.py show-forecast-data
Show alert warnings data:

bash
Copy code
python lib/cli.py show-alert-warnings
and same for other tables


COMMANDS FOR NAVIGATING THE TABLES ARE STORED IN CLI.PY 
TYPE PYTHON LIB/CLI.PY.