# Exercise 1: Your First Product Catalog

zoblik_catalog = {
    "PROD001": {
        "name": "Zoblik Smartwatch",
        "price": 199.99,
        "quantity":50,
        "category": "Wearables"
    },
    "PROD002": {
        "name": "Zoblik Wireless Earbuds",
        "price": 79.99,
        "category": "Audio"
    },
    "PROD003": {
        "name": "Zobli k Wireless Headphones",
        "price": 82.9,
        "category": "Audio"
    }
}

# Access and print the name of PROD001
print(f"Product name for PROD001: {zoblik_catalog['PROD001']['name']}")

# Access and print the price of PROD002
print(f"Product price for PROD002: ${zoblik_catalog['PROD002']['price']}")

#Access and print the quantity of PROD001
print(f"Product quantity for PROD001: {zoblik_catalog['PROD001']['quantity']}")