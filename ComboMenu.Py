def Order_Donut():
    attempts = 0
    Donut_Not_Selected = True
    while Donut_Not_Selected:
        order = input ("Which one would you like?")
        if order == " Chocolate Frosted":
            return (order, 2.50)
        elif order == " Strawberry Frosted":
            return (order, 3.50)
        elif order == " Boston Creme":
            return (order, 3.00)
        else:
            print ("Sorry, we don't serve that here")
        attempts +=1
        if attempts == 3:
            print ("Please Go Away, Your holding up the Line")    
            break
    return (None, 0.0)

donut_type = False
Dozen_Time = True
double_donut = False
Donut_Hole_choice = False
Sugar_Price = 0
max_value = 10
min_value = 0
fry_choice = False
drink_choice = False
Order_Total = 0
Drink_Attempts = 0
print ("Hello, Welcome To Krispy Kreme, unfortunately were low on donuts and only have") 
print ("Chocolate Frosted, Strawberry Frosted, and Boston Creme.")
first_choice, cost = Order_Donut()
Order_Total += cost
doublethat = input ("Would you like any other donuts?")
if doublethat == " Yes":
        second_choice, cost = Order_Donut()
        doublethat
        third_choice, cost = Order_Donut() 
        Order_Total += cost
elif doublethat == " No":
        donut_type == True
while donut_type == True:
    drink = input ("Would you like a Coffee with that?")
    if drink == " Yes" :
        drink_choice = True
        break
    elif drink == " No" or " no" :  
        Dozen_Time = True
        NoCoffee = ("")
        break
    else:
        print ("Sorry, I don't know what your talking about")   
        exit()
while drink_choice == True :
    drink_size = input ("Okay, Would you like A Small, A Medium, Or A Large?")
    if drink_size == " A Small" :
        print ("Okay, That will be an additional 1.00$")
        Order_Total += 1.00
        Dozen_Time = True
        break
    elif drink_size == " A Medium" or " a medium" :
        print ("Okay, That will be an additional 1.75$")
        Order_Total += 1.75
        Dozen_Time = True
        break
    elif drink_size == " A Large" or " a large" :
        print ("Okay, That will be an additional 2.25")
        Order_Total += 2.25
        Dozen_Time = True
        break
print (f"Okay, So far your order total is {Order_Total:.2f}$")
if Dozen_Time == True :
    DonutHoles = input ("Would you like Donut Holes with that as well?")
    if DonutHoles == " Yes" :
        Donut_Hole_choice = True
    elif DonutHoles == " No" or " no" :  
        h = True
    else:
        print ("Sorry, I don't know what your talking about")   
        exit()
while Donut_Hole_choice == True :
    Donut_Hole_Amount = input ("Okay, Would you like Four, a Half a Dozen, Or a Dozen?")
    if Donut_Hole_Amount == " Four" :
        Mega_Small = input ("Are you sure you don't want a Dozen?")
        if Mega_Small == " Yes":
            print ("Okay that will be an additional 2:00$")
            h = True
            break
        else:
            print ("Okay, That will be an additional 1.00$")
            Order_Total += 1.00
            h = True
            break
    elif Donut_Hole_Amount == " A Half a Dozen" or " a half a dozen" or" a Half a Dozen" :
        print ("Okay, That will be an additional 1.75$")
        Order_Total += 1.50
        h = True
        break
    elif Donut_Hole_Amount == " a Dozen" or " A Dozen" or " a dozen" :
        print ("Okay, That will be an additional 2.25")
        Order_Total += 2.00
        h = True
        break
print (f"Okay, So far your order total is {Order_Total:.2f}$")
while h == True :
    Sugar = input ("Would you like sugar in your Coffee?, only 25 cents a packet.")
    if Sugar == " Yes":
        Sugar_Size = int(input("How much Sugar would you liKe?"))
        if int(Sugar_Size) > 10:
            print ("Do you want to die of obesity?, Try Again...")
        if 0 < int(Sugar_Size) <= 10:
            print (f"Okay, {Sugar_Size} packets for you")
            print (f"Okay that will be {Sugar_Size * 0.25 }$")
            Sugar_Price = int(Sugar_Size) * .25
            Order_Total + Sugar_Price
            break
print (f"Okay, So far your order total is {Order_Total:.2f}$")
print (f"Okay, So far you have ordered {order}, You said{drink} to{drink_size} coffee")
print (f"You also said {Dozen_Time} and got{Donut_Hole_Amount} Donut Holes")
print (f"Furthermore, you said{Sugar} to sugar and got {Sugar_Size}")