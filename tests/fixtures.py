import json

def products_fixture():
    return [
        {
            "code": "VOUCHER",
            "name": "Voucher",
            "unit_price": {
                "amount": "5.00",
                "currency_code": "EUR",
            },
        },
        {
            "code": "TSHIRT",
            "name": "T-shirt",
            "unit_price": {
                "amount": "20.00",
                "currency_code": "EUR",
            },
        },
        {
            "code": "MUG",
            "name": "Coffee mug",
            "unit_price": {
                "amount": "7.50",
                "currency_code": "EUR",
            }
        }
    ]

def discounts_fixture():
    return {
        "VOUCHER": {
            "product": "VOUCHER",
            "active": "2X1",
            "available_discounts": {
                "2X1": {
                    "code": "2X1",
                    "type": "package",
                    "qty": 2,
                    "price": {
                        "amount": "5.00",
                        "currency_code": "EUR",
                    }
                }
            }
        },
        "TSHIRT": {
            "product": "TSHIRT",
            "active": "BULKAFTER3",
            "available_discounts": {
                "BULKAFTER3":{
                    "code": "BULKAFTER3",
                    "type": "bulk",
                    "min_qty": 3,
                    "unit_price": {
                        "amount": "19.00",
                        "currency_code": "EUR",
                    }
                }
            }
        }
    }

def price_rules_fixture():
    return {
        "products": products_fixture(),
        "product_discounts": discounts_fixture()
    }

def price_rules_json_fixture():
    rules = price_rules_fixture()
    return json.dumps(rules)
