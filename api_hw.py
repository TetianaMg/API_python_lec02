from storage_hw import save_to_disk, remove_files, save_to_avro
import requests
import os
import json

API_URL = 'https://fake-api-vycpfa6oca-uc.a.run.app/'
AUTH_TOKEN = os.environ['AUTH_TOKEN']

if not AUTH_TOKEN:
    print("AUTH_TOKEN environment variable must be set")


def transform_files(stg_dir: str, raw_dir: str):
    remove_files(stg_dir)
    list_files = os.listdir(raw_dir)
    for in_file in list_files:
        with open(raw_dir + '\\' + in_file, 'r', encoding='utf-8') as f:
            result = f.read()
            records = json.loads(result)
            save_to_avro(records,stg_dir, in_file )


def get_sales(date: str, raw_dir: str):
    remove_files(raw_dir)
    page_nbr = 1
    while True:
        response = requests.get(
            url= f"{API_URL}sales?date={date}&page={page_nbr}",
            headers={'Authorization': AUTH_TOKEN}
        )
        if response.status_code != 404:
            print("Response status code:", response.status_code)
            print("Response JSON", response.json())
            print("Page number", page_nbr)
            save_to_disk(response.text, raw_dir, date, page_nbr)
            page_nbr += 1
        else:
            return


