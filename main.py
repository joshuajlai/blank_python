import sqlite3
from sqlite_tutorial import *

def make_tables(connection, schema_file):
    file_pointer = open(schema_file, 'r')
    contents = file_pointer.read()
    commands = contents.split(';')
    for command in commands:
        command = command.strip()
        cursor = connection.cursor()
        cursor.execute(command)



schema_file = 'schema.sql'
connection = sqlite3.connect('db/database.db')
make_tables(connection, schema_file)
project_dao = models.Project(connection)
project_dao.insert_project("test")
print(project_dao.find_project_by_name("test"))
