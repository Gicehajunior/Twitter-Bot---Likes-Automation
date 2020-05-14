
class User:
    connection = ""
    database_connection = ""
    username = ""
    password = ""
    table = "Users"
    # instantiate the class user
    def __init__(self, connection, database_connection,  username, password):
        self.connection = connection
        self.database_connection = database_connection
        self.username = username
        self.password = password
    
    def create_table(self):
        with self.connection:
            sql = """CREATE TABLE Users(
                Uid text,
                username text,
                password longText
            )"""
        
            self.database_connection.execute(sql)

            # save the database by commiting
            self.connection.commit()

            self.connection.close()

    def save_user(self):
        with self.connection:
            db_cursor = self.database_connection
            db_cursor.execute("INSERT INTO Users VALUES(:Uid, :username, :password)", {'Uid': self.username, 'username': self.username, 'password': self.password})
            
            action = self.connection
            action.commit()
            
            # action.close()
            
    def fetch_user(self):
        with self.connection:
            db_cursor = self.database_connection
            db_cursor.execute("SELECT * FROM Users")
            
            db_cursor = self.database_connection
            
            # fetch all the users 
            users = db_cursor.fetchall()
            
            connection = self.connection
            connection.commit()
            
            # connection.close()
            return users
        
    def activate_user_bot(self):
        with self.connection:
            db_cursor = self.database_connection
            db_cursor.execute("SELECT * FROM Users WHERE username=:username", {'username':self.username})
            
            connection = self.connection
            connection.commit()
            while True:
                user_credentials = [
                    self.username,
                    self.password
                    ]
                
                return user_credentials
            else:
                return

