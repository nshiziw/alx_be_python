purchase_amount = float(input("Enter your purchase amount: "))
if purchase_amount >= 10000:
    discount = 0.1;
elif purchase_amount >= 5000:
    discount = 0.05;
else:
    discount = 0;

final_price = purchase_amount * (1 - discount)
print("Final price after discount is: " + str(final_price))