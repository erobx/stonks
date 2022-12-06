import sqlite3
import click
import csv
from flask import current_app, g

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row
    
    return g.db

def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

# going to run once a week or however often we want to populate the db
def init_db():
    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        print('Loading db')
        file = open('../test.csv')
        contents = csv.reader(file)
        insert_records = "INSERT INTO stock (logo, ticker, pe, volume, price, market_cap, eps, sector, employees, revenue, growth, profit) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
        db.executemany(insert_records, contents)
        select_all = "SELECT ticker, price, sector FROM stock"
        rows = db.execute(select_all).fetchall()
        for r in rows:
            print(r)
        db.commit()

@click.command('init-db')
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)