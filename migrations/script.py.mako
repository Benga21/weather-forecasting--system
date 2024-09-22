<%
from alembic import context
from sqlalchemy import engine_from_config, pool
from sqlalchemy.ext.declarative import DeclarativeMeta
from logging.config import fileConfig

# Interpret the config file for Python logging.
# This line sets up loggers basically.
fileConfig(context.config.config_file_name)
target_metadata = None

def run_migrations_offline():
    """Run migrations in 'offline' mode.
    This configures the context with just a URL and not an Engine,
    though an Engine is acceptable here as well.
    By skipping the Engine creation we don't even need a database
    to be available.
    """
    url = context.config.get_main_option("sqlalchemy.url")
    context.configure(url=url, target_metadata=target_metadata)

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    """Run migrations in 'online' mode.
    In this scenario we need to create an Engine and associate a
    connection with the context.
    """
    connectable = engine_from_config(
        context.config.get_section(context.config.config_ini_section),
        prefix='sqlalchemy.',
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()

