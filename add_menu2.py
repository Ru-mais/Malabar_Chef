import json

new_categories = [
  {
    "category": "SEA FOOD DISHES",
    "color": "#00BCD4",
    "items": [
      { "name": "Fish roast", "price": "20", "cal": "320", "rating": "4.8", "macros": { "p": "30g", "c": "5g", "f": "15g" }, "image": "/images/curry.png" },
      { "name": "Fish masala", "price": "20", "cal": "340", "rating": "4.7", "macros": { "p": "28g", "c": "8g", "f": "18g" }, "image": "/images/curry.png" },
      { "name": "Fish curry", "price": "20", "cal": "270", "rating": "4.9", "macros": { "p": "25g", "c": "10g", "f": "12g" }, "image": "/images/curry.png" },
      { "name": "Fish molly", "price": "20", "cal": "290", "rating": "4.8", "macros": { "p": "24g", "c": "12g", "f": "14g" }, "image": "/images/curry.png" },
      { "name": "Fish Tawa fry", "price": "20", "cal": "310", "rating": "4.9", "macros": { "p": "32g", "c": "2g", "f": "16g" }, "image": "/images/plate.png" },
      { "name": "Fish Pollichathu", "price": "22", "cal": "380", "rating": "4.9", "macros": { "p": "35g", "c": "8g", "f": "18g" }, "image": "/images/plate.png" },
      { "name": "Fish Mango curry", "price": "25", "cal": "260", "rating": "4.8", "macros": { "p": "28g", "c": "15g", "f": "10g" }, "image": "/images/curry.png" },
      { "name": "Prawn roast", "price": "25", "cal": "370", "rating": "4.7", "macros": { "p": "30g", "c": "8g", "f": "20g" }, "image": "/images/plate.png" },
      { "name": "Elaneer paal konju", "price": "25", "cal": "280", "rating": "4.9", "macros": { "p": "25g", "c": "12g", "f": "15g" }, "image": "/images/curry.png" },
      { "name": "Fish mulakittathu", "price": "10", "cal": "150", "rating": "4.6", "macros": { "p": "20g", "c": "5g", "f": "4g" }, "image": "/images/curry.png" }
    ]
  },
  {
    "category": "VEG DISHES",
    "color": "#4CAF50",
    "items": [
      { "name": "Paneer butter masala", "price": "18", "cal": "380", "rating": "4.8", "macros": { "p": "18g", "c": "20g", "f": "25g" }, "image": "/images/curry.png" },
      { "name": "Chilly paneer", "price": "18", "cal": "340", "rating": "4.7", "macros": { "p": "16g", "c": "22g", "f": "20g" }, "image": "/images/plate.png" },
      { "name": "Mix veg", "price": "8", "cal": "220", "rating": "4.5", "macros": { "p": "8g", "c": "25g", "f": "10g" }, "image": "/images/curry.png" },
      { "name": "Chilly gopi", "price": "16", "cal": "250", "rating": "4.6", "macros": { "p": "5g", "c": "30g", "f": "12g" }, "image": "/images/plate.png" },
      { "name": "Gopi manchurian", "price": "16", "cal": "260", "rating": "4.8", "macros": { "p": "6g", "c": "32g", "f": "12g" }, "image": "/images/plate.png" },
      { "name": "Mushroom masala", "price": "14", "cal": "290", "rating": "4.7", "macros": { "p": "10g", "c": "20g", "f": "18g" }, "image": "/images/curry.png" },
      { "name": "Dal fry", "price": "8", "cal": "180", "rating": "4.6", "macros": { "p": "12g", "c": "28g", "f": "4g" }, "image": "/images/curry.png" },
      { "name": "Chana Masala", "price": "8", "cal": "130", "rating": "4.5", "macros": { "p": "10g", "c": "22g", "f": "3g" }, "image": "/images/curry.png" }
    ]
  }
]

with open('app/data/menu.json', 'r') as f:
    existing = json.load(f)

existing.extend(new_categories)

with open('app/data/menu.json', 'w') as f:
    json.dump(existing, f, indent=2)
