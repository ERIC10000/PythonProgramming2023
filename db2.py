# UPDATE: modify an already existing record.
import pymysql
# Step1. Database connection
connection = pymysql.connect(host='localhost', user = 'root', password='', database='MpesaTestDB')
print("Database connected successfully")

# cursor
cursor = connection.cursor()


# data
salary = 1200000
emp_id = 9

# sql 
sql = "update employees set salary = %s where emp_id = %s" 

# execution
data = (salary, emp_id)

cursor.execute(sql, data)
connection.commit()

# notify user
print(f"Employee ID {emp_id} salary updated successfully with {salary}")