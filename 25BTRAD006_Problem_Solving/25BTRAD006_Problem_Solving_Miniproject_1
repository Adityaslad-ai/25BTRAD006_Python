print("========== BILL GENERATOR ==========")

name = input("Enter customer name: ")

item1 = input("Enter item 1 name: ")
price1 = float(input("Enter price of item 1: "))
qty1 = int(input("Enter quantity: "))

item2 = input("Enter item 2 name: ")
price2 = float(input("Enter price of item 2: "))
qty2 = int(input("Enter quantity: "))

item3 = input("Enter item 3 name: ")
price3 = float(input("Enter price of item 3: "))
qty3 = int(input("Enter quantity: "))

total1 = price1 * qty1
total2 = price2 * qty2
total3 = price3 * qty3

subtotal = total1 + total2 + total3
gst = subtotal * 0.18
grand_total = subtotal + gst

print("\n========== BILL ==========")
print("Customer Name:", name)
print("--------------------------")
print("Item\tQty\tAmount")
print("--------------------------")
print(item1, "\t", qty1, "\t", total1)
print(item2, "\t", qty2, "\t", total2)
print(item3, "\t", qty3, "\t", total3)
print("--------------------------")
print("Subtotal:", subtotal)
print("GST (18%):", gst)
print("Grand Total:", grand_total)
print("==========================")
print("Thank you for shopping!")
