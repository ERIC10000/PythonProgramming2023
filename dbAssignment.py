# 1. create a database connection to
# 2. confirm the connection
# INSERT INTO : signup, job application, booking.....
import pymysql
connection = pymysql.connect(host='localhost', user = 'root', password='', database='MpesaTestDB')
print("Database connected successfully")

# create 3 variable to hold, username, password, phone

username = "Chris"
password = "12345"
phone = "+254740922861"

# 4. create a cursor to your connection
cursor = connection.cursor()
# 5. write sql to save username, password and phone on users table
sql = "insert into  users (username, password, phone) values (%s, %s, %s)"
# 6. Execute your sql
data = (username, password, phone)
cursor.execute(sql, data)
# 7. commit yoiur connection 
connection.commit()
# 8. notify that record has been saved.
print("User Saved Successfully")


# SELECTS: Login, Ecommerce.....
# update
# DELETE


# FLASK: Python framework to run web applications