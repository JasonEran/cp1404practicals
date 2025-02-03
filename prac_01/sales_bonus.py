"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
LOW_BONUS_RATE = 0.1
HIGH_BONUS_RATE = 0.15
BONUS_THRESHOLD = 1000

sales = float(input("Enter sales: "))

while sales >= 0:
    if sales < BONUS_THRESHOLD:
        bonus = sales * LOW_BONUS_RATE
    else:
        bonus = sales * HIGH_BONUS_RATE
    print(f"Your bonus is: ${bonus:.2f}")
    sales = float(input("Enter sales: "))
print("The bonus calculation has been completed. Thank you for using it")