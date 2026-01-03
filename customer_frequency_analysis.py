frequent_threshold = 5

customers = {
    "C001": 2,
    "C002": 7,
    "C003": 5,
    "C004": 1,
    "C005": 9
}

for customer_id in customers:

    purchase_count = customers[customer_id]

    if purchase_count >= frequent_threshold:
        print(customer_id, "=> Frequent Buyer")
    else:
        print(customer_id, "=> Non-Frequent Buyer")
