import os
import time
import requests


BASE_DIR = os.environ.get("BASE_DIR")

if not BASE_DIR:
    print("BASE_DIR environment variable must be set")
    exit(1)

JOB2_PORT = 8082

RAW_DIR = os.path.join(BASE_DIR, "raw", "sales", "2022-08-09")
print(RAW_DIR)

STG_DIR = os.path.join(BASE_DIR, "stg", "sales", "2022-08-09")
print(STG_DIR)


def run_job2(stg_dir, raw_dir):
    print("Starting job2:")
    resp = requests.post(
        url=f'http://localhost:{JOB2_PORT}/',
        json={
            "raw_dir": raw_dir,
            "stg_dir": stg_dir
        }
    )
    assert resp.status_code == 201
    print("job2 completed!")


if __name__ == '__main__':
    run_job2(STG_DIR,RAW_DIR)
