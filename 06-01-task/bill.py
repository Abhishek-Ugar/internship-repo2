def bill(units):
    if units < 100 :
        res = units * 2
        print(res)
    elif units > 100 and units < 200 :
        res = units * 4
        print(res)
    elif units > 200 :
        res = units * 6
        print(res)
    else:
        print("enter valid input..!")
        


