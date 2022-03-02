# JavaScript object  Notation

import json
from pathlib import Path

cars = [
    {"Brand": "Nissan", "Price": 45.000, "Color": "Blue"},
    {"Brand": "Ford", "Price": 75.000, "Color": "Green"},
    {"Brand": "Ferrari", "Price": 117.000, "Color": "Yellow"},
]

cars_json = json.dumps(cars)
Path("cars.json").write_text(cars_json)

file_cars_json = Path("cars.json").read_text()
json_file = json.loads(cars_json)
print(json_file[2]['Brand'])