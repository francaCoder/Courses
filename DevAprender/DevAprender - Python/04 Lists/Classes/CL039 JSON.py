import json
from pathlib import Path

cars = [
    {"Brand": "Nissan", "Price": 45.000, "Color": "Blue"},
    {"Brand": "Ford", "Price": 75.000, "Color": "Red"},
    {"Brand": "BMW", "Price": 115.000, "Color": "Gray"},
]

cars_json = json.dumps(cars)
Path('cars_json').write_text(cars_json)

file_cars_json = Path('cars_json').read_text()
file_json = json.loads(file_cars_json)
print(f"{file_json[0]['Brand']} {file_json[0]['Price']}")