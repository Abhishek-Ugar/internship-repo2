opening_stock=[80,100,220,350]
closing_stock=[100,200,300,400]
for i in range(len(opening_stock)):
    if opening_stock[i] > closing_stock[i]:
        print("product[i+1]:stock increased")
    elif closing_stock[i] > opening_stock[i]:
        print("procduct[i+1]:stock decreased")
    else:
        print("product[i+1]:stock unchanged")

