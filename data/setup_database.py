import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from lib.db.models import Base
engine = create_engine('sqlite:///data/weather_data.db', connect_args={'timeout': 10})
DATABASE_URL = "sqlite:///data/weather_data.db"
def ensure_data_directory_exists():
    directory = 'data'
    if not os.path.exists(directory):
        os.makedirs(directory)
        print(f"Directory '{directory}' created.")
    else:
        print(f"Directory '{directory}' already exists.")
def setup_database():
    engine = create_engine(DATABASE_URL)
    Base.metadata.create_all(engine)  # this Creates all  the tables
if __name__ == "__main__":
    ensure_data_directory_exists()  
    setup_database()
    print("Database and tables created successfully.")
