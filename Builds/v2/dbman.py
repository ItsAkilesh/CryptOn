import pymysql 
import os
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='root',
                             autocommit=True)
                    

cursor = connection.cursor()

