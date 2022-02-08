"""
Show on screen the "ability" "lightning-rod" from pikachu.json
"""

import json
from pathlib import Path


file_pikachu_json = Path('pikachu_json').read_text()
file_json = json.loads(file_pikachu_json)
print(f"{file_json['abilities'][1]['ability']['name']}")