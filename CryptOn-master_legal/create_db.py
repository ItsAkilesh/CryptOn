import dbman
def create():
    dbman.cursor.execute("CREATE DATABASE IF NOT EXISTS CRYPTON;")
def profiles():
    dbman.cursor.execute("CREATE TABLE IF NOT EXISTS PROFILES(USERNAME TEXT, PASSWORD TEXT);")
def db_select():
    dbman.cursor.execute("USE CRYPTON;")                    
def users(username):
    dbman.cursor.execute(f"CREATE TABLE IF NOT EXISTS {username}(enc_text longtext, enc_key longtext);")
