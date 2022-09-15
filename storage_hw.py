"""
Layer of persistence. Save content to outer world here.
"""
import json
import os
import shutil
from fastavro import writer, parse_schema


schema = {
    'name': 'Purchase',
    'type': 'record',
    'fields': [
        {'name': 'client', 'type': 'string'},
        {'name': 'purchase_date', 'type': 'string'},
        {'name': 'product', 'type': 'string'},
        {'name': 'price', 'type': 'float'}
    ]
}

parsed_schema = parse_schema(schema)


def save_to_avro(content: str, path: str, file_name: str):
    file_name = file_name.split(".")[0]
    file_name = f"{file_name}.avro"
    os.makedirs(path, exist_ok=True)
    with open(os.path.join(path, file_name), 'wb') as out:
        writer(out, parsed_schema, content)


def remove_files(path: str):
    if os.path.isdir(path):
        shutil.rmtree(path)


def save_to_disk(json_content: str, path: str, date: str, page_nbr: int):
    file_name = f"sales_{date}_{page_nbr}.json"
    os.makedirs(path, exist_ok=True)
    with open(os.path.join(path, file_name), 'w') as f:
        f.write(json_content)



