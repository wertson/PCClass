lc_PRICE = 99.00
lv_quantity = 0
lv_discountAmount = 0.00
lv_subtotal = 0.00
lv_totalSavings = 0.00
lv_total = 0.00

lv_quantity = int(input("Enter the quantity of packages: "))

if lv_quantity <= 9:
	lv_total = lv_quantity * lc_PRICE
	print("You owe: ", lv_total, "You dont get a discount")

elif lv_quantity <=19:
	lv_subtotal = lv_quantity * lc_PRICE
	lv_discountAmount = lv_subtotal * 0.10
	lv_total = lv_subtotal - lv_discountAmount
	print("Subtotal: ", lv_subtotal)
	print("You had a 10% discount which would be: ", lv_discountAmount) 
	print("You owe: ", lv_total)
	
elif lv_quantity <=49:
	lv_subtotal = lv_quantity * lc_PRICE
	lv_discountAmount = lv_subtotal * 0.20
	lv_total = lv_subtotal - lv_discountAmount
	print("Subtotal: ", lv_subtotal)
	print("You had a 20% discount which would be: ", lv_discountAmount) 
	print("You owe: ", lv_total)
	
elif lv_quantity <=99:
	lv_subtotal = lv_quantity * lc_PRICE
	lv_discountAmount = lv_subtotal * 0.30
	lv_total = lv_subtotal - lv_discountAmount
	print("Subtotal: ", lv_subtotal)
	print("You had a 30% discount which would be: ", lv_discountAmount) 
	print("You owe: ", lv_total)

elif lv_quantity >=100:
	lv_subtotal = lv_quantity * lc_PRICE
	lv_discountAmount = lv_subtotal * 0.40
	lv_total = lv_subtotal - lv_discountAmount
	print("Subtotal: ", lv_subtotal)
	print("You had a 40% discount which would be: ", lv_discountAmount) 
	print("You owe: ", lv_total)

