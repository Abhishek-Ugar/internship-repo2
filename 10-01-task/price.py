prices=[150,250,350]
total=0
for price in prices:
    total=total+price
    average=total/len(prices)

    print("total order value:",total)
    print("average item prices:",average)

