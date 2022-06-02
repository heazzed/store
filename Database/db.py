import sqlite3


class Database:

    db_name = 'sqlite_python.db'
    connection = False

    def connect(self):
        try:
            self.connection = sqlite3.connect(self.db_name)
            print("Соединение с базой данных {0} установлено".format(self.db_name))
        except sqlite3.Error as error:
            print("Ошибка при подключении к базе данных {0} ".format(self.db_name))
            print(error)

    def disconnect(self):
        if self.connection:
            self.connection.close()
            print("Соединение с базой данных {0} закрыто".format(self.db_name))

    def select_script(self, script):
        cursor = self.connection.cursor()
        cursor.execute(script)
        result = cursor.fetchall()
        cursor.close()
        return result
