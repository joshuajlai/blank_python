class Project():
    def __init__(self, connection):
        self.connection = connection

    def insert_project(self, project_name):
        cursor = self.connection.cursor()
        cursor.execute(
            "insert into projects (project_name) values (?)",
            [project_name]
        )
        return cursor.lastrowid

    def find_project_by_name(self, project_name):
        cursor = self.connection.cursor()
        cursor.execute(
            "select * from projects where project_name = ?",
            [project_name]
        )
        rows = cursor.fetchall()
        return next(iter(rows), None)
