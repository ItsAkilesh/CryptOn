import dbman
dbman.cursor.execute("CREATE DATABASE IF NOT EXISTS CRYPTON;")
dbman.cursor.execute("USE CRYPTON;")       
dbman.cursor.execute("CREATE TABLE IF NOT EXISTS PROFILES(USERNAME TEXT, PASSWORD TEXT);")                     
dbman.cursor.execute("CREATE TABLE IF NOT EXISTS CRYPT(USERNAME TEXT, enc_text text, enc_key INTEGER);")
