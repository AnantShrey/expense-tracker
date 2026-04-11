from config import DB_CONFIG
import mysql.connector

# Connect to db
# Create table
# insert expenses (amount, category, date)
# fetch all expenses
# delete expenses

def get_connection():
    return mysql.connector.connect(**DB_CONFIG)