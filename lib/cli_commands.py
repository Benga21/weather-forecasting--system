import click

@click.group()
def cli():
    """A simple CLI application."""
    pass

@click.command()
def custom_command():
    """A custom CLI command."""
    click.echo("Custom command executed! 🎉")

@click.command()
def another_command():
    """Another command."""
    click.echo("Another command executed! 🚀")

@click.command()
@click.argument('name')
def greet(name):
    """Greet a user by name."""
    click.echo(f"Hello, {name}! 👋")

# Add commands to the CLI group
cli.add_command(custom_command)
cli.add_command(another_command)
cli.add_command(greet)

if __name__ == "__main__":
    cli()
