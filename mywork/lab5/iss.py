#!/usr/bin/env python
import requests
import json
import pandas as pd
import sys
import logging
import os
import time
import mysql.connector

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
logging.basicConfig(level=logging.INFO, handlers=[console_handler])


URL="http://api.open-notify.org/iss-now.json"


def get_db_connection():
    try:
        db = mysql.connector.connect(
            host=os.getenv("DBHOST"),
            user=os.getenv("DBUSER"),
            password=os.getenv("DBPASS"),
            database=os.getenv("DBNAME", "iss")
        )
        logging.info("Connected")
        return db
    except mysql.connector.Error as e:
        logging.error(f"Database connection failed: {e}")
        sys.exit(1)

def register_reporter(table, reporter_id, reporter_name):
    db = None
    cursor = None

    try:
        db = get_db_connection()
        cursor = db.cursor()

        check_sql = f"SELECT reporter_id FROM {table} WHERE reporter_id = %s"
        cursor.execute(check_sql, (reporter_id,))
        result = cursor.fetchone()

        if result is None:
            insert_sql = f"INSERT INTO {table} (reporter_id, reporter_name) VALUES (%s, %s)"
            cursor.execute(insert_sql, (reporter_id, reporter_name))
            db.commit()
            logging.info(f"Inserted {reporter_id}")
        else:
            logging.info(f" {reporter_id} already exists")

    except mysql.connector.Error as e:
        logging.error(f"Database error in register_reporter: {e}")

    finally:
            cursor.close()
            db.close()
def parse_args():
    try:
        json_file = sys.argv[1]
        csv_file = sys.argv[2]
    except IndexError:
        logging.error(f"Usage: python {sys.argv[0]} <json_file> <csv_file>")
        sys.exit(1)
    return json_file, csv_file



def extract(url,json_file):
    logging.info(f"getting  data from{url}")
    try:
        response = requests.get(url)
        response.raise_for_status() # raise an exception for HTTP errors
        data = response.json()
        
        with open(json_file, 'w') as f:
            json.dump(data, f, indent=2)
        logging.info(f"Extracted raw data and saved to {json_file}")
    except requests.exceptions.HTTPError as e:
        logging.error(f"HTTP error occurred:", e)
    except requests.exceptions.RequestException as e:
        logging.error(f"A request error occurred:", e)
    except Exception as e:
        logging.error(f"An unexpected error occurred:", e)
    return  data


def transform(record):
    df = pd.json_normalize(record)

    df["timestamp"] = pd.to_datetime(
        df["timestamp"],
        unit="s"
    ).dt.strftime("%Y-%m-%d %H:%M:%S")

    return df

def load(df, reporter_id):
    db = None
    cursor = None

    try:
        db = get_db_connection()
        cursor = db.cursor()

        sql = """
        INSERT INTO locations (message, latitude, longitude, timestamp, reporter_id)
        VALUES (%s, %s, %s, %s, %s)
        """

        message = df["message"][0]
        latitude = float(df["iss_position.latitude"][0])
        longitude = float(df["iss_position.longitude"][0])
        timestamp = df["timestamp"][0]

        values = (message, latitude, longitude, timestamp, reporter_id)

        cursor.execute(sql, values)
        db.commit()

        logging.info("Inserted")




    except mysql.connector.Error as e:
        logging.error(f"Database error in load: {e}")

    finally:
        if cursor is not None:
            cursor.close()
        if db is not None:
            db.close()



if __name__ == "__main__":
    reporter_id = "ama8us"
    reporter_name = "Ruixin Duan"

    register_reporter("reporters", reporter_id, reporter_name)
    for i in range(10):
        logging.info(f"Times {i+1}")

        record = extract(URL, "iss.json")
        df = transform(record)

        load(df, reporter_id)

        time.sleep(1)