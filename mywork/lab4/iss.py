#!/usr/bin/env python
import requests
import json
import pandas as pd
import sys
import logging
import os
import time

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
logging.basicConfig(level=logging.INFO, handlers=[console_handler])


URL="http://api.open-notify.org/iss-now.json"

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

def load(df, csv_file):
        if os.path.exists(csv_file):
            old_df = pd.read_csv(csv_file)
            combined = pd.concat([old_df, df], ignore_index=True)
            combined.to_csv(csv_file, index=False)
            logging.info(f"Appended 1 row to existing CSV: {csv_file}")

        else:
            df.to_csv(csv_file, index=False)
            logging.info(f"Created CSV: {csv_file}")



if __name__ == "__main__":
    json_file, csv_file = parse_args()
    for i in range(10):
        logging.info(f"Times {i+1}")
        record = extract(URL, json_file)
        df = transform(record)
        load(df, csv_file)

        time.sleep(1)