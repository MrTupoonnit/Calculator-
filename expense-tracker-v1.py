import datetime
expenses = {  }
while True :
	item = input("What did you spend on('Q' to quit):  ")
	if item.upper() == "Q":
		break 
	amount= int(input(f"How much did you spend on {item}: MWK "))
	expenses.update({(item): (amount)})

amounts = expenses.values()	
total = sum(amounts)
print("=" * 7,datetime.date.today(), "=" * 11,)
print(f"ITEM			AMOUNT")
for item, amount in expenses.items() :
		print(f"{item}			MWK{amount}")
print(f"TOTALS = MWK{total: ,}")
		
		
		
		
