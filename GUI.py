from tkinter import *
import time
from includes import database
from includes import credentials
import bot

# global scope declaration of variables
username= ""
password = ""
signup_screen = ""
screen = ""
username_entry = ""
password_entry = ""
connection = ""
db_connection = ""
login_username = ""
login_password = ""
login_username_entry = ""
login_password_entry = ""

# save credentials instance
def save_credentials():
    username_info = username.get()
    password_info = password.get()

    global connection
    global db_connection
    
    # db connection
    connection = database.conn()
    db_connection = database.cursor_connection(connection)

    User = credentials.User(connection, db_connection, username_info, password_info)
    User.create_table()
    User.save_user()

    Label(signup_screen, text="registered successfully! Go back to login window to activate the bot", fg="green", font=("Calibri", 11)).pack()
    
    #print(User.fetch_user())
    
# activate bot 
def activate_bot():
    # user_credential = ""
    login_username_info = login_username.get()
    login_password_info = login_password.get()
    
    # db connection
    connection = database.conn()
    db_connection = database.cursor_connection(connection)

    #bot activation credentials
    User = credentials.User(connection, db_connection, login_username_info, login_password_info)
    
    # list of user credentials returned
    user_credentials = User.activate_user_bot()
    
    # access username and password from the tuple
    users_username = user_credentials[0]
    users_password = user_credentials[1]
    
    # print the credentials
    ### print(users_username)
    ### print(users_password)
    
    # activate the bot
    my_bot = bot.TwitterBOT(users_username, users_password)
    my_bot.login()
    my_bot.like_tweets('AndelaKenya')

def register_user():
    global signup_screen
    signup_screen = Toplevel(screen)
    signup_screen.title("Register Account")
    signup_screen.geometry("450x500")
    
    # Label(text = "Twitter Bot", bg="gray", width="400", height="2", font=("Calibri", 13)).pack()
    Label(text = "").pack()
    Label(text = "").pack()
    
    # globalise username&password&the entries
    global username
    global password
    global username_entry
    global password_entry
    
    # declare some datatypes to variables/declare variables.
    username = StringVar()
    password = StringVar()
    
    Label(signup_screen, text = "").pack()
    Label(signup_screen, text = "").pack()
    Label(signup_screen, text = "").pack()
    
    Label(signup_screen, text = "Please Register Below To Continue", font=("Calibri", 13)).pack()
    Label(signup_screen, text = "").pack()
    Label(signup_screen, text = "").pack()
    
    Label(signup_screen, text = "Username * ").pack()
    username_entry = Entry(signup_screen, textvariable = username)
    username_entry.pack()
    
    Label(signup_screen, text = "").pack()
    
    Label(signup_screen, text = "Password * ").pack()
    password_entry = Entry(signup_screen, textvariable = password) 
    password_entry.pack()
    
    Label(signup_screen, text = "").pack()
    Label(signup_screen, text = "").pack()
    Label(signup_screen, text = "").pack()
    Button(signup_screen, text="Signup", width="10", height="1", command=save_credentials).pack()
    


def main_win():
    global screen
    screen = Tk()
    screen.geometry("450x500")
    
    # screen title
    screen.title("Twitter Likes Automation Bot V1.0")
    
    Label(text = "Twitter Bot", bg="gray", width="400", height="2", font=("Calibri", 13)).pack()
    Label(text = "").pack()
    Label(text = "").pack()
    
    # globalise username&password&the entries
    global login_username
    global login_password
    global login_username_entry
    global login_password_entry
    
    # inputs: for user interface
    # declare some datatypes to variables/declare variables.
    login_username = StringVar()
    login_password = StringVar()
    
    Label(text = "Twitters Username * ").pack()
    login_username_entry = Entry(textvariable = login_username)
    login_username_entry.pack()
    
    Label(text = "").pack()
    
    Label(text = "Twitters Password * ").pack()
    login_password_entry = Entry(textvariable = login_password) 
    login_password_entry.pack()
    
    # extra labels
    Label(text="").pack()
    # login button 
    Button(text="Activate Bot", width="30", height="2", command = activate_bot ).pack()
    Label(text="").pack()
    
    # signup button link
    Button(text="Save Twitters Credentials on Bot", width="30", height="2", command=register_user).pack()
    Label(text="").pack()
    Label(text="Forgot Password? Click here", font=("Calibri", 13)).pack()

    screen.mainloop()

main_win()

