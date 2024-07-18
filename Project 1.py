print("-" * 40)
print("            Billing System")
print("-" * 40)

name = input ("Please Enter Your Name:")
bill_amount = float(input("Please Enter The Bill Amount:"))

tip = bill_amount * 0.10
gst = bill_amount *0.20
total_bill = bill_amount + tip + gst

print(f"\nTip (10%): {tip}")
print (f"GST (20%): {gst}")
print(f"Total Bill: {total_bill}\n")

cash_received = float(input("Please Enter CAsh Received:"))
change = cash_received - total_bill

print("-" * 40)
print(f"Name: {name}")
print(f"Bill Amount: {bill_amount}")
print(f"Tip: {tip}")
print(f"GST: {gst}")
print(f"Total Bill: {total_bill}")
print(f"Cash Received: {cash_received}")
print(f"Change: {change}")
print("-" * 40)
print("              Thank you!")
print("-" * 40)