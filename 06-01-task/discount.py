# Task
# Create a function:
# calculate_discount(price, customer_type)

# 5/100 * price

# Discount Rules
# Regular → 5%
# Premium → 15%
# Employee → 25%

# Expected Output

# Return final price after discount.

def calculate_discount(price, customer_type):
    if customer_type == "Regular" :
        res = 5/100 * price
        print(res)
    if customer_type == "Premium" :
        res = 15/100 * price
        print(res)
    if customer_type == "Employee" :
        res = 25/100 * price
        print(res)


calculate_discount(250, "Regular")