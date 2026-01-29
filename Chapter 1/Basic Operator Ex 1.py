#Exercise 1: Zoblik Sales Commission Calculation
# Initial values
#user inputs
monthly_sales=float(input("Enter the monthly sales: "))
Commission_rate= float(input("Enter the commissions (in %): ")) /100
#fixed data
bonus_threshold= 20000
bonus_amount=500
#calculate the base commission
base_commission = monthly_sales *Commission_rate
print(f"Base Commission: ₹{base_commission}")
#check if bonus threshold was met and add bonus if so
if monthly_sales >= bonus_threshold:
    total_commission=base_commission+bonus_amount
    print(f"Congrats! Sales target met! Total commission (with bonus): ₹ {total_commission}")
else:
    total_commission=base_commission
    print(f"Sales target not met! Total Commission: ₹ {total_commission}")