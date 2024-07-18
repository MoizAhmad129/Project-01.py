print("*" * 40)
print("Billing System")
print("*" * 40)

name = input("Please enter your name: ")
bill_amount = float(input("Please enter the bill amount: "))

tip = bill_amount * 0.10
gst = bill_amount * 0.20
total_bill = bill_amount + tip + gst

print(f"\nTip (10%): {tip:.2f}")
print(f"GST (20%): {gst:.2f}")
print(f"Total Bill: {total_bill:.2f}\n")

cash_received = float(input("Please enter cash received: "))
change = cash_received - total_bill

print("*" * 40)
print(f"Name: {name}")
print(f"Bill: {bill_amount:.2f}")
print(f"Tip: {tip:.2f}")
print(f"GST: {gst:.2f}")
print(f"Total Bill: {total_bill:.2f}")
print(f"Cash Received: {cash_received:.2f}")
print(f"Change: {change:.2f}")
print("*" * 40)
print("Thank you for dining with us!")
print("*" * 40)