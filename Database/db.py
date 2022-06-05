import sqlite3


class Database:

    db_name = 'sqlite_python.db'
    connection = False
    is_connected = False

    def connect(self):
        try:
            if self.is_connected is False:
                self.connection = sqlite3.connect(self.db_name)
                self.is_connected = True
                print("Соединение с базой данных {0} установлено".format(self.db_name))
            else:
                print("Соединение уже было установлено")
        except sqlite3.Error as error:
            print("Ошибка при подключении к базе данных {0} ".format(self.db_name))
            print(error)

    def disconnect(self):
        if self.is_connected is True:
            self.connection.close()
            self.is_connected = False
            print("Соединение с базой данных {0} закрыто".format(self.db_name))

    def select_script(self, script):
        cursor = self.connection.cursor()
        cursor.execute(script)
        result = cursor.fetchall()
        cursor.close()
        return result

    def insert_script(self, script):
        cursor = self.connection.cursor()
        try:
            cursor.execute(script)
            self.connection.commit()
            print("Товар успешно добавлен в базу данных")
        except sqlite3.Error as error:
            print("При добавлении товара в базу данных произошла ошибка")
            print(error)
        cursor.close()
