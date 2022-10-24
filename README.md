# Novicap Checkout Code Challenge Solution in Python3

## Problem ([Source](https://novicap.com/en/code-challenge/)):
 Let’s say that, besides providing invoice finance, Novicap runs a physical store which sells 3 products:

|Code         | Name         |  Price    |
|-------------|--------------|-----------|
|VOUCHER      | Voucher      |   5.00€   |
|TSHIRT       | T-shirt      |  20.00€   |
|MUG          | Coffee mug   |   7.50€   |

Various departments have suggested some discounts to improve sales:

1. The marketing department wants a 2-for-1 special on VOUCHER items.
2. The CFO insists that the best way to increase sales is with (tiny) discounts on bulk purchases. If you buy 3 or more TSHIRT items, the price per unit should be 19.00€.

The checkout process allows for items to be scanned in any order, and calculates the total price. The interface looks like this (in ruby):
```
checkout = Checkout.new(price_rules)
checkout.scan("VOUCHER")
checkout.scan("VOUCHER")
checkout.scan("TSHIRT")
price = checkout.total
```

**Examples:**
```
Items: VOUCHER, TSHIRT, MUG
Total: 32.50€
Items: VOUCHER, TSHIRT, VOUCHER
Total: 25.00€
Items: TSHIRT, TSHIRT, TSHIRT, VOUCHER, TSHIRT
Total: 81.00€
Items: VOUCHER, TSHIRT, VOUCHER, VOUCHER, MUG, TSHIRT, TSHIRT
Total: 74.50€
```
Our team will add, remove, and change products and discounts, so they should be configurable with a JSON file. They’re definitely going to get creative with the discounts in the next session.

## Solution Assumptions:

The current version of the solution was implemented with the following assumptions in mind:
- The `price_rules` input is a valid JSON string defining the products and the products discounts available.
- A particular product can only have up to one discount.
- Only two types of discounts exists for now: "package" and "bulk" which were used to implement the **1.** and **2.** discounts in the **Problem** section respectively.
- The `total` output is a string representing the amount and the currency symbol.

## Setup:

### Requirements:

 - Python v3.8.5+ 

Create and activate a virtualenv:
```
virtualenv --p=python3 .env
```
Install requirements:
```
pip install -r requirements.txt
```

## Usage:

To use the checkout library in a python console (in the root director) or in another python script, use the following import:
```
from src import Checkout
```
Then it can be used in the following fashion (analogous to the interface in ruby defined in the **Problem** section):
```
checkout = Checkout(price_rules)
checkout.scan("VOUCHER")
checkout.scan("VOUCHER")
checkout.scan("TSHIRT")
price = checkout.total
```
