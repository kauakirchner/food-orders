import click
from src.app import create_app
from flask.cli import with_appcontext
from src.app.db import populate_db, delete_tables

app = create_app()

@click.command(name='populate_db')
@with_appcontext
def call_command():
  populate_db()

@click.command(name='delete_tables')
@with_appcontext
def drop_tables():
  delete_tables()

app.cli.add_command(call_command)
app.cli.add_command(delete_tables)

if __name__ == "__main__":
  app.run()
