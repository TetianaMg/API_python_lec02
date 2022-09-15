import os
import requests


BASE_DIR = os.environ.get("BASE_DIR")

if not BASE_DIR:
    print("BASE_DIR environment variable must be set")
    exit(1)

JOB1_PORT = 8081

RAW_DIR = os.path.join(BASE_DIR, "raw", "sales", "2022-08-09")
print(RAW_DIR)

STG_DIR = os.path.join(BASE_DIR, "stg", "sales", "2022-08-09")
print(STG_DIR)


def run_job1(raw_dir):
    print("Starting job1:")
    resp = requests.post(
        url=f'http://localhost:{JOB1_PORT}/',
        json={
            "date": "2022-08-09",
            "raw_dir": raw_dir
        }
    )
    assert resp.status_code == 201
    print("job1 completed!")


if __name__ == '__main__':
    run_job1(RAW_DIR)
