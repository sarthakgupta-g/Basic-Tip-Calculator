bill=float(input("How much was your bill?"))
tip_percent=float(input("What percent tip do you want to pay?"))

tip=tip_percent*bill*0.01
total=tip+bill

print(f"Your tip is: ${tip:.2f}")
print(f"Your total is: ${total:.2f}")
