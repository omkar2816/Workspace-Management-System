import mysql.connector


class Connection:
    _instance = None

    def __new__(cls, *args, **kwargs):
        try:
            if not cls._instance:
                cls._instance = super().__new__(cls)
                cls._instance.cnx = mysql.connector.connect(
                    user='root',
                    password='Omkar@2802',
                    host='localhost',
                    port='3306',
                    database='wms'
                )
            return cls._instance
        except mysql.connector.Error as e:
            print("Connection failed", e)

    @staticmethod
    def get_connection(self):
        # return self.cnx
        return connection._instance.cnx

if __name__ == "__main__":
    connection = Connection()
