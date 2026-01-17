import pandas as pd
import mysql.connector

# 1. Load CSV file
df = pd.read_csv("../data/hotel_bookings_sample_550.csv")

print("CSV Loaded Successfully")
print("Total Records:", len(df))

# 2. Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",          # or 'root'
    password="admin",        # use your actual password
    database="hotel_db"
)

cursor = conn.cursor()

# 3. Insert data row by row
insert_query = """
INSERT INTO hotel_bookings
(hotel, is_canceled, lead_time, arrival_date_year, arrival_date_month,
 arrival_date_day_of_month, country, market_segment, adr, total_guests,
 stays_in_week_nights, stays_in_weekend_nights)
VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
"""

for _, row in df.iterrows():
    cursor.execute(insert_query, tuple(row))

# 4. Commit changes
conn.commit()

print("Data inserted successfully!")

# 5. Close connection
cursor.close()
conn.close()
