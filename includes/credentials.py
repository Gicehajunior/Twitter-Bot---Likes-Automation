import hashlib
import base64 as BS
import uuid
# import bcrypt

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

    def save_user(self):
        with self.connection:
            db_cursor = self.database_connection
            
            db_cursor.execute("SELECT * FROM Users WHERE username=:Uid", {'Uid':self.username})
            user = db_cursor.fetchone()
            new_user = [(self.username, self.username, self.password)]
            # sorted_user_details = user[0]
            # sorted_new_user_details = new_user[0]
            
            if user == new_user:
                print('Username has already been taken')
                return
            else:
                # hashing the password
                #  encode bytes 
                # salt = BS.urlsafe_b64encode(uuid.uuid4().bytes)
                
                # # using hash library generate sha512 for the salt generated
                # salt_sha = hashlib.sha512()
                
                # # update the password using the salt and salt_sha generated above
                # salt_sha.update(str(self.password)+ str(salt))
                
                # # hashed password
                # hashed_password = BS.urlsafe_b64encode(salt_sha.digest())
                
                # hashed_password = self.password
                
                #run sql
                db_cursor.execute("INSERT INTO Users VALUES(:Uid, :username, :password)", {'Uid': self.username, 'username': self.username, 'password': self.password})
                
                action = self.connection
                action.commit()
                
                # action.close()
            # else:
                        
            
    def fetch_user(self):
        with self.connection:
            db_cursor = self.database_connection
            db_cursor.execute("SELECT * FROM Users")
            
            # fetch all the users 
            users = db_cursor.fetchall()
            
            connection = self.connection
            connection.commit()
            
            # connection.close()
            return users
        
    def activate_user_bot(self):
        with self.connection:
            db_cursor = self.database_connection
            db_cursor.execute("SELECT * FROM Users WHERE username=:Uid", {'Uid':self.username})
            
            row = db_cursor.fetchone()
            connection = self.connection
            connection.commit()
            
            while True:
                return
            else:
                return row

