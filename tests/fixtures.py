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
        "VOUCHER": [
            {
                "code": "VOUCHER2x1",
                "type": "package",
                "qty": 2,
                "unit_price": {
                    "amount": "2.50",
                    "currency_code": "EUR",
                }
            }
        ],
        "TSHIRT": [
            {
                "code": "TSHIRTBULK3",
                "type": "bulk",
                "tiers": [
                    {
                        "min_qty": 3,
                        "max_qty": None,
                        "unit_price": {
                            "amount": "19.00",
                            "currency_code": "EUR",
                        }
                    }
                ]
            }
        ]
    }

def price_rules_fixture():
    return {
        "products": products_fixture(),
        "discounts": discounts_fixture()
    }

def price_rules_json_fixture():
    rules = price_rules_fixture()
    return json.dumps(rules)
