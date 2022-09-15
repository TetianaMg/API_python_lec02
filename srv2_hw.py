"""
This file contains the controller that accepts command via HTTP
and trigger business logic layer
"""

from flask import Flask, request
from flask import typing as flask_typing

import api_hw

app = Flask(__name__)

@app.route('/', methods=['POST'])
def main() -> flask_typing.ResponseReturnValue:
    """
    Controller that accepts command via HTTP and
    trigger business logic layer

    Proposed POST body in JSON:
    {
      "data: "2022-08-09",
      "raw_dir": "/path/to/my_dir/raw/sales/2022-08-09"
    }
    """
    input_data: dict = request.json
    stg_dir = input_data.get('stg_dir')
    raw_dir = input_data.get('raw_dir')

    if not raw_dir or not stg_dir:
        return {
            "message": "dir parameter missed",
        }, 400

    api_hw.transform_files(stg_dir, raw_dir)

    return {
               "message": "Data transformed successfully",
           }, 201


if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=8082)