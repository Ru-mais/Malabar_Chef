import json
import urllib.parse

with open('app/data/menu.json', 'r') as f:
    data = json.load(f)

for category in data:
    for item in category['items']:
        clean_name = item['name'].replace(' ', ',')
        url = f"https://loremflickr.com/600/800/{clean_name},food/all"
        item['image'] = url

with open('app/data/menu.json', 'w') as f:
    json.dump(data, f, indent=2)
print("Updated menu.json with dynamic image URLs.")
