import json

new_categories = [
  {
    "category": "BREAKFAST",
    "color": "#FFC107",
    "items": [
      { "name": "Chapati", "price": "1", "cal": "120", "rating": "4.5", "macros": { "p": "4g", "c": "22g", "f": "2g" }, "image": "/images/porotta.png" },
      { "name": "Porotta", "price": "1", "cal": "160", "rating": "4.8", "macros": { "p": "5g", "c": "30g", "f": "6g" }, "image": "/images/porotta.png" },
      { "name": "Poori baji", "price": "6", "cal": "280", "rating": "4.7", "macros": { "p": "6g", "c": "45g", "f": "10g" }, "image": "/images/plate.png" },
      { "name": "Idiappam", "price": "1", "cal": "110", "rating": "4.6", "macros": { "p": "3g", "c": "25g", "f": "1g" }, "image": "/images/plate.png" },
      { "name": "Puttu", "price": "3", "cal": "180", "rating": "4.8", "macros": { "p": "5g", "c": "38g", "f": "2g" }, "image": "/images/plate.png" },
      { "name": "Neer dosa", "price": "1", "cal": "130", "rating": "4.5", "macros": { "p": "4g", "c": "28g", "f": "1g" }, "image": "/images/plate.png" },
      { "name": "Ghee roast", "price": "6", "cal": "340", "rating": "4.9", "macros": { "p": "6g", "c": "40g", "f": "18g" }, "image": "/images/plate.png" },
      { "name": "Idali", "price": "5", "cal": "80", "rating": "4.6", "macros": { "p": "3g", "c": "18g", "f": "0g" }, "image": "/images/plate.png" },
      { "name": "Masala dosa", "price": "6", "cal": "320", "rating": "4.8", "macros": { "p": "8g", "c": "45g", "f": "12g" }, "image": "/images/plate.png" },
      { "name": "Onion roast", "price": "6", "cal": "300", "rating": "4.7", "macros": { "p": "6g", "c": "42g", "f": "14g" }, "image": "/images/plate.png" },
      { "name": "Uthappam", "price": "6", "cal": "220", "rating": "4.6", "macros": { "p": "7g", "c": "35g", "f": "6g" }, "image": "/images/plate.png" },
      { "name": "Vada", "price": "1", "cal": "180", "rating": "4.5", "macros": { "p": "6g", "c": "20g", "f": "8g" }, "image": "/images/plate.png" }
    ]
  },
  {
    "category": "CHICKEN DISHES",
    "color": "#E53935",
    "items": [
      { "name": "Chicken pepper", "price": "17", "cal": "320", "rating": "4.7", "macros": { "p": "30g", "c": "10g", "f": "15g" }, "image": "/images/curry.png" },
      { "name": "Chicken roast", "price": "17", "cal": "380", "rating": "4.8", "macros": { "p": "32g", "c": "12g", "f": "20g" }, "image": "/images/curry.png" },
      { "name": "Chicken varutharachathu", "price": "18", "cal": "410", "rating": "4.9", "macros": { "p": "34g", "c": "15g", "f": "24g" }, "image": "/images/curry.png" },
      { "name": "Chicken kadai", "price": "18", "cal": "350", "rating": "4.7", "macros": { "p": "30g", "c": "14g", "f": "18g" }, "image": "/images/curry.png" },
      { "name": "Chicken ularthiyathu", "price": "18", "cal": "370", "rating": "4.9", "macros": { "p": "35g", "c": "10g", "f": "22g" }, "image": "/images/curry.png" },
      { "name": "Chicken kondattam", "price": "18", "cal": "290", "rating": "4.6", "macros": { "p": "28g", "c": "15g", "f": "12g" }, "image": "/images/curry.png" },
      { "name": "Butter chicken", "price": "18", "cal": "430", "rating": "4.9", "macros": { "p": "28g", "c": "20g", "f": "26g" }, "image": "/images/curry.png" },
      { "name": "Chicken kuruma", "price": "16", "cal": "380", "rating": "4.7", "macros": { "p": "26g", "c": "18g", "f": "22g" }, "image": "/images/curry.png" },
      { "name": "Chicken stew", "price": "16", "cal": "280", "rating": "4.8", "macros": { "p": "25g", "c": "22g", "f": "10g" }, "image": "/images/curry.png" },
      { "name": "Chilly chicken", "price": "17", "cal": "360", "rating": "4.7", "macros": { "p": "28g", "c": "25g", "f": "16g" }, "image": "/images/curry.png" },
      { "name": "Chicken manchurian", "price": "18", "cal": "340", "rating": "4.6", "macros": { "p": "26g", "c": "28g", "f": "14g" }, "image": "/images/curry.png" },
      { "name": "Garlic chicken", "price": "18", "cal": "330", "rating": "4.7", "macros": { "p": "28g", "c": "20g", "f": "15g" }, "image": "/images/curry.png" },
      { "name": "Ginger chicken", "price": "18", "cal": "325", "rating": "4.6", "macros": { "p": "28g", "c": "22g", "f": "14g" }, "image": "/images/curry.png" },
      { "name": "Chicken chettinad", "price": "18", "cal": "395", "rating": "4.8", "macros": { "p": "30g", "c": "15g", "f": "22g" }, "image": "/images/curry.png" },
      { "name": "Nadan chicken curry", "price": "13", "cal": "310", "rating": "4.8", "macros": { "p": "26g", "c": "12g", "f": "16g" }, "image": "/images/curry.png" }
    ]
  },
  {
    "category": "BIRYANI",
    "color": "#FBC02D",
    "items": [
      { "name": "Chicken Dum Biryani", "price": "15", "cal": "650", "rating": "4.8", "macros": { "p": "40g", "c": "70g", "f": "22g" }, "image": "/images/signature_biryani.png" },
      { "name": "Chicken Leghorn Biryani", "price": "16", "cal": "620", "rating": "4.7", "macros": { "p": "38g", "c": "65g", "f": "20g" }, "image": "/images/signature_biryani.png" },
      { "name": "Chicken Fried Biryani", "price": "16", "cal": "580", "rating": "4.6", "macros": { "p": "35g", "c": "60g", "f": "18g" }, "image": "/images/signature_biryani.png" },
      { "name": "Mutton Dum Biryani", "price": "22", "cal": "600", "rating": "4.9", "macros": { "p": "42g", "c": "65g", "f": "25g" }, "image": "/images/signature_biryani.png" },
      { "name": "Beef Dum Biryani", "price": "17", "cal": "560", "rating": "4.8", "macros": { "p": "38g", "c": "60g", "f": "20g" }, "image": "/images/signature_biryani.png" },
      { "name": "Fish Biryani", "price": "20", "cal": "610", "rating": "4.7", "macros": { "p": "35g", "c": "65g", "f": "18g" }, "image": "/images/signature_biryani.png" },
      { "name": "Chicken Hyderabadi Biryani", "price": "20", "cal": "700", "rating": "4.8", "macros": { "p": "45g", "c": "75g", "f": "28g" }, "image": "/images/signature_biryani.png" },
      { "name": "Chicken Madghout (qtr/half)", "price": "13/24", "cal": "500", "rating": "4.7", "macros": { "p": "35g", "c": "55g", "f": "15g" }, "image": "/images/signature_biryani.png" },
      { "name": "Mandi Rice with chicken tawa fry (qtr/half)", "price": "15/26", "cal": "480", "rating": "4.8", "macros": { "p": "38g", "c": "50g", "f": "18g" }, "image": "/images/signature_biryani.png" }
    ]
  },
  {
    "category": "MILK SHAKES",
    "color": "#9C27B0",
    "items": [
      { "name": "Avocado", "price": "12", "cal": "180", "rating": "4.9", "macros": { "p": "3g", "c": "20g", "f": "12g" }, "image": "/images/signature_falooda.png" },
      { "name": "Mango", "price": "12", "cal": "160", "rating": "4.8", "macros": { "p": "2g", "c": "35g", "f": "1g" }, "image": "/images/signature_falooda.png" },
      { "name": "Banana", "price": "10", "cal": "150", "rating": "4.6", "macros": { "p": "2g", "c": "32g", "f": "1g" }, "image": "/images/signature_falooda.png" },
      { "name": "Strawberry", "price": "12", "cal": "130", "rating": "4.7", "macros": { "p": "1g", "c": "28g", "f": "1g" }, "image": "/images/signature_falooda.png" },
      { "name": "Pappaya", "price": "12", "cal": "120", "rating": "4.5", "macros": { "p": "1g", "c": "25g", "f": "0g" }, "image": "/images/signature_falooda.png" },
      { "name": "Apple", "price": "10", "cal": "140", "rating": "4.6", "macros": { "p": "1g", "c": "30g", "f": "1g" }, "image": "/images/signature_falooda.png" },
      { "name": "Date", "price": "12", "cal": "170", "rating": "4.8", "macros": { "p": "2g", "c": "38g", "f": "1g" }, "image": "/images/signature_falooda.png" },
      { "name": "Mixed dry fruit", "price": "12", "cal": "220", "rating": "4.9", "macros": { "p": "5g", "c": "40g", "f": "6g" }, "image": "/images/signature_falooda.png" },
      { "name": "ICECREAM MILK SHAKES", "price": "10", "cal": "400", "rating": "4.7", "macros": { "p": "6g", "c": "55g", "f": "18g" }, "image": "/images/signature_falooda.png" },
      { "name": "SPECIAL MILK SHAKES", "price": "12", "cal": "600", "rating": "4.9", "macros": { "p": "8g", "c": "80g", "f": "25g" }, "image": "/images/signature_falooda.png" }
    ]
  },
  {
    "category": "RICE AND NOODLES",
    "color": "#FF9800",
    "items": [
      { "name": "Jeera rice", "price": "12", "cal": "320", "rating": "4.6", "macros": { "p": "5g", "c": "65g", "f": "4g" }, "image": "/images/plate.png" },
      { "name": "Saffron rice", "price": "15", "cal": "340", "rating": "4.8", "macros": { "p": "5g", "c": "68g", "f": "4g" }, "image": "/images/plate.png" },
      { "name": "Ghee rice", "price": "8", "cal": "380", "rating": "4.7", "macros": { "p": "4g", "c": "65g", "f": "12g" }, "image": "/images/plate.png" },
      { "name": "White rice", "price": "6", "cal": "260", "rating": "4.5", "macros": { "p": "4g", "c": "58g", "f": "1g" }, "image": "/images/plate.png" },
      { "name": "Fried rice (Veg/Chicken/Mix)", "price": "16", "cal": "400", "rating": "4.7", "macros": { "p": "12g", "c": "65g", "f": "10g" }, "image": "/images/plate.png" },
      { "name": "Schezwan fried rice (Veg/Chicken/Mix)", "price": "16", "cal": "430", "rating": "4.8", "macros": { "p": "14g", "c": "68g", "f": "12g" }, "image": "/images/plate.png" },
      { "name": "Noodles (Veg/Chicken/Mix)", "price": "16", "cal": "370", "rating": "4.6", "macros": { "p": "10g", "c": "60g", "f": "8g" }, "image": "/images/plate.png" },
      { "name": "Schezwan noodles (Veg/Chicken/Mix)", "price": "18", "cal": "410", "rating": "4.7", "macros": { "p": "12g", "c": "65g", "f": "10g" }, "image": "/images/plate.png" }
    ]
  },
  {
    "category": "BREAD",
    "color": "#795548",
    "items": [
      { "name": "Chapati", "price": "1", "cal": "90", "rating": "4.5", "macros": { "p": "3g", "c": "18g", "f": "1g" }, "image": "/images/porotta.png" },
      { "name": "Porotta", "price": "1", "cal": "250", "rating": "4.9", "macros": { "p": "6g", "c": "35g", "f": "10g" }, "image": "/images/porotta.png" },
      { "name": "Appam", "price": "1.5", "cal": "110", "rating": "4.7", "macros": { "p": "2g", "c": "22g", "f": "1g" }, "image": "/images/porotta.png" },
      { "name": "Muttyappam", "price": "1.5", "cal": "150", "rating": "4.6", "macros": { "p": "3g", "c": "30g", "f": "2g" }, "image": "/images/porotta.png" },
      { "name": "Neypathal", "price": "1.5", "cal": "180", "rating": "4.8", "macros": { "p": "4g", "c": "35g", "f": "3g" }, "image": "/images/porotta.png" },
      { "name": "Wheat Porotta", "price": "1.5", "cal": "200", "rating": "4.6", "macros": { "p": "6g", "c": "30g", "f": "6g" }, "image": "/images/porotta.png" },
      { "name": "Pathiri", "price": "1", "cal": "47", "rating": "4.7", "macros": { "p": "1g", "c": "10g", "f": "0g" }, "image": "/images/porotta.png" },
      { "name": "Neer Dosa", "price": "1", "cal": "90", "rating": "4.5", "macros": { "p": "3g", "c": "18g", "f": "1g" }, "image": "/images/plate.png" }
    ]
  }
]

with open('app/data/menu.json', 'r') as f:
    existing = json.load(f)

existing.extend(new_categories)

with open('app/data/menu.json', 'w') as f:
    json.dump(existing, f, indent=2)
