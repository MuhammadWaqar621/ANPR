import psycopg2
import time
from datetime import datetime, timezone
#Establishing the connection
conn = psycopg2.connect(
   database="Surveillance", user='postgres', password='admin12345', host='127.0.0.1', port= '5432'
)
#Setting auto commit false
conn.autocommit = True

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

# Preparing SQL queries to INSERT a record into the database.

# Create a table
# cursor.execute('''CREATE TABLE TEST (id SERIAL PRIMARY KEY, DETECTED_NUMBERPLATE TEXT, Date timestamptz)''')

dt = datetime.now(timezone.utc)
plate_num='ABC 12 777'
# inserting values
cursor.execute('insert into TEST values (DEFAULT,  %s, %s)', (plate_num, dt))

dt = datetime.now(timezone.utc)

# Commit your changes in the database
conn.commit()
print("Records inserted........")

# Closing the connection
conn.close()