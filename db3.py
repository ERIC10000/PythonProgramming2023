# DELETE
# connection
import pymysql
# Step1. Database connection
connection = pymysql.connect(host='localhost', user = 'root', password='', database='MpesaTestDB')
print("Database connected successfully")

# cursor
cursor = connection.cursor()

emp_id = 4

sql = "delete from employees where emp_id = %s"

cursor.execute(sql, emp_id)
connection.commit()
print("Record Deleted Successfully")