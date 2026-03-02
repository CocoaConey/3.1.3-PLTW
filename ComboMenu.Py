attempts = 0
while True:
    order = input ("Which one would you like?")
    if order == " Chicken" :
        print ("Okay,That will be 2.50$")
        burger_type = True
    elif order == " Beef":
        print ("Okay,That will be 3.50$")
        burger_type = True
    elif order == " Veggie":
        print ("Okay,That will be 3.00$")
        burger_type = True
    else:
        print ("Sorry, we don't serve that here")
    attempts +=1
    if attempts == 3:
        print ("Please Go Away, Your holding up the Line")    
        break