def price_rules_fixture():
    return [
        {
            "code": "VOUCHER",
            "name": "Voucher",
            "price_models": {
                "unit_price": {
                    "amount": "5.00",
                    "currency_code": "EUR",
                },
                "package": {
                    "qty": 2,
                    "unit_price": {
                        "amount": "2.50",
                        "currency_code": "EUR",
                    }
                },
            }
        },
        {
            "code": "TSHIRT",
            "name": "T-shirt",
            "price_models": {
                "unit_price": {
                    "amount": "20.00",
                    "currency_code": "EUR",
                },
                "bulk_tiers": [
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
        },
        {
            "code": "MUG",
            "name": "Coffee mug",
            "price_models": {
                "unit_price": {
                    "amount": "7.50",
                    "currency_code": "EUR",
                }
            }
        }
    ]