# READ OPERATION(SELECT ): Retrieving data from the Database
import pymysql
# Step1. Database connection
connection = pymysql.connect(host='localhost', user = 'root', password='', database='MpesaTestDB')
print("Database connected successfully")

# Step2. Create a connection cursor
cursor = connection.cursor()

# Step3. Sql to read data
sql = "select * from employees"

# Execute
cursor.execute(sql)

# Step4. Check whether its empty(rowcount)
count = cursor.rowcount
print(count)

if count == 0:
    print("No records founds")
else:
    data = cursor.fetchall()
    print(data)