import MySQLdb
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get database credentials from .env
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD", "password")
DB_NAME = os.getenv("DB_NAME", "mydb")

# Establish connection
try:
    connection = MySQLdb.connect(
        host=DB_HOST,
        user=DB_USER,
        passwd=DB_PASSWORD,
        db=DB_NAME
    )
    print("Connected to the database!")
except MySQLdb.MySQLError as e:
    print("f Connection error: {e}")
    exit()


def fetch_top_3_events():
    query = """
    SELECT e.id, e.name, e.date, e.total_tickets, 
           COALESCE(SUM(t.quantity), 0) AS total_tickets_sold
    FROM event e
    LEFT JOIN ticket t ON e.id = t.event_id
    GROUP BY e.id, e.name, e.date, e.total_tickets
    ORDER BY total_tickets_sold DESC
    LIMIT 3;
    """

    with connection.cursor(MySQLdb.cursors.DictCursor) as cursor:
        cursor.execute(query)
        result = cursor.fetchall()

        for row in result:
            print(row)


fetch_top_3_events()

connection.close()
