revenue=float(input("Enter the revenue: "))
expenses=float(input("Enter the expenses: "))
profit=revenue-expenses 
if revenue>expenses:
    print("Profit:",profit)
elif revenue<expenses:
    print("Loss:",(profit))
else:
    print("No profit, no loss")
