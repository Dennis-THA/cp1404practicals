
LOW_BONUS = 10
HIGH_BONUS = 15

"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
sales_amount = float(input("Enter sales: $"))
while sales_amount >= 0:
    if sales_amount >= 1000:
        sales_bonus = sales_amount * (HIGH_BONUS / 100)
    else:
        sales_bonus = sales_amount * (LOW_BONUS / 100)
    print(sales_bonus)
    sales_amount = float(input("Enter sales: $"))
print("Invalid input")
