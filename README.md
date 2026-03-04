attempts = 0
while True:
    order = input ("Which one would you like?")
    if order == " Chicken" :
        print ("Okay,That will be 2.50$")
        burger_type = True
        break
    elif order == " Beef":
        print ("Okay,That will be 3.50$")
        burger_type = True
        break
    elif order == " Veggie":
        print ("Okay,That will be 3.00$")
        burger_type = True
        break
    else:
        print ("Sorry, we don't serve that here")
    attempts +=1
    if attempts == 3:
        print ("Please Go Away, Your holding up the Line")    
        exit()
if burger_type == True:
    drink = input ("Would you like a drink with that?")
    if drink == " Yes" :
        drink_choice = True
    elif drink == " No" :  
        Total_Check = True
    else:
        print ("Sorry, I don't know what your talking about")
if drink_choice == True :
    drink_size = input ("Okay, Would you like Small, Medium, Or Large?")
    if drink_size == " Small" :
        print ("Okay, That will be an additional 1:00$")
    elif drink_size == " Medium " :
        print ("Okay, That will be an additional 1.75$")
    elif drink_size == " Large " :
        print ("Okay, That will be an additional 2.25")
