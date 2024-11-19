import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)
cursor = connection.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS feedback_analysis;")
cursor.execute("USE feedback_analysis;")
cursor.execute("""
CREATE TABLE IF NOT EXISTS feedback (
    id INT AUTO_INCREMENT PRIMARY KEY,
    url TEXT,
    content TEXT,
    sentiment FLOAT
);
""")
connection.commit()
cursor.close()
connection.close()
print("Base de données et table créées avec succès !")
