# Integrating MySQL database with Python
# Module: pymysql

import pymysql

# 1. Create database connection
# connect(host='', user = '', password = '', database = '')

connection = pymysql.connect(host='localhost', user = 'root', password='', database='MpesaTestDB')
print("Database connected successfully")

# 2. Inserting Data to the Tables

employee_name = "Sarah Ann Cornor"
hire_date = '2023-07-04'
salary = 200000
department = 2

# cursor: A cursor is a property(state) used to execute sql codes on python files
# prepared statements(%s): They indicate that values will be passed during sql exec

cursor = connection.cursor()

sql = "insert into employees (emp_name, hire_date, salary, dept_id) values (%s, %s, %s, %s)"

# 3. Sql execution:
data = (employee_name, hire_date, salary, department)
cursor.execute(sql, data)

# commit: saving changes to the database
connection.commit()


print("Record saved successfully")
