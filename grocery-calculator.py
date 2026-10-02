#This is a file I made when my mom was talking about making calculations for our home grocery shop 


items = [ ]
prices = [ ]
sell_prices = [ ]

while True :
	item = input("Please Enter the Name of the item:  ")
	price = int(input(f"What is the price of {item}:  "))
	sell_price = price + (price * 0.15)
	items.append(item)
	prices.append(price)
	sell_prices.append(sell_price )

	choice = input("Would you like to add another item ? (Y/N):  ")
	if choice.upper()== "N":	
		for item, price, sell_price  in zip(items, prices,sell_prices) :
			print(f"Item: {item} - Cost price: {price} - Selling price: {sell_price} ")
	
		break


			
				
				
		