import mysql.connector

# Connect to MySQL
connection = mysql.connector.connect(
    host="localhost",       # MySQL server host (use 'localhost' for local server)
    user="root",            # MySQL username (use 'root' if you haven't created a new user)
    password="XO;)Fh@ckoppl69", # Replace with your MySQL root password
    database="MySQL80"  # Optional: You can specify the database or leave it empty
)

# Check if connection is successful
if connection.is_connected():
    print("Successfully connected to MySQL")

# Create a cursor object to interact with the database
cursor = connection.cursor()

# Example: Show all databases
cursor.execute("SHOW DATABASES")

# Fetch and print all databases
databases = cursor.fetchall()
for database in databases:
    print(database)

# Close the connection
cursor.close()
connection.close()
