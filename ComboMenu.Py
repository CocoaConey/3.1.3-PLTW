while True:
    drink_size = "None"
    orders = ["", "", "", 0]
    donut_index = 0
    drink_index = 1
    holes_index = 2
    sugar_index = 3
    donut_total = 0
    drink_total = 0
    End_Order = False
    donut_type = False
    Hole_Order_Total = 0
    Dozen_Time = True
    initial = True
    Donut_Hole_choice = False
    Donut_Hole_Amount = "None"
    Sugar_Price = 0
    max_value = 10
    min_value = 0
    fry_choice = False
    drink_choice = False
    attempts = 0
    Order_Total = 0
    Drink_Attempts = 0
    Sugar_Size = 0
    print ("Hello, Welcome To Krispy Kreme, unfortunately were low on donuts and only have") 
    print ("Chocolate Frosted, Strawberry Frosted, and Boston Creme.")
    while initial == True:
        order = input ("Which one would you like?")
        if order == " Chocolate Frosted":
            print ("Okay,That will be 3.656186...$")
            Order_Total += 3.65618638176481684611687416816
            donut_total += 1
            donut_type = True
            initial = False
        elif order == " Strawberry Frosted":
            print ("Okay,That will be 3.55$")
            Order_Total += 3.55
            donut_total += 1
            donut_type = True
            initial = False
        elif order == " Boston Creme":
            print ("Okay,That will be 3.50$")
            Order_Total += 3.50
            donut_total += 1
            donut_type = True
            initial = False
        else:
            print ("Sorry, we don't serve that here")
        attempts +=1
        if attempts == 3:
            print ("Please Go Away, Your holding up the Line")    
            break
    while donut_type == True:
        drink = input ("Would you like a Coffee with that?")
        if drink == " Yes" :
            drink_choice = True
            drink_total += 1
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
            Donut_Hole_Amount = " No"
            h = True
        else:
            print ("Sorry, I don't know what your talking about")   
            exit()
    while Donut_Hole_choice == True :
        Donut_Hole_Amount = input ("Okay, Would you like Four, a Half a Dozen, Or a Dozen?")
        if Donut_Hole_Amount == " Four" :
            Mega_Small = input ("Are you sure you don't want a Dozen?")
            if Mega_Small == " Yes":
                print ("Okay that will be an additional 2.00$")
                Hole_Order_Total += 1
                Order_Total += 2
                h = True
                break
            else:
                print ("Okay, That will be an additional 1.00$")
                Order_Total += 3.00
                Hole_Order_Total += 1
                h = True
                break
        elif Donut_Hole_Amount == " A Half a Dozen" or " a half a dozen" or" a Half a Dozen" :
            print ("Okay, That will be an additional 1.75$")
            Order_Total += 1.50
            Hole_Order_Total += 1
            h = True
            break
        elif Donut_Hole_Amount == " a Dozen" or " A Dozen" or " a dozen" :
            print ("Okay, That will be an additional 2.25")
            Order_Total += 2.00
            Hole_Order_Total += 2.00
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
                Order_Total += Sugar_Price
                h = False
                End_Order = True
        elif Sugar == " No":
            h = False
            End_Order = True
    while End_Order == True:       
        orders[donut_index] = order
        orders[drink_index] = drink_size
        orders[holes_index] = Donut_Hole_Amount
        orders[sugar_index] = Sugar_Size
        print ("you ordered:")
        print (orders)
        break
    if donut_total + drink_total + Hole_Order_Total >= 3.00:
        print ("You ordered the combo and saved one dollar!")
        Order_Total -= 1.00
        print (f"Your final total is {Order_Total:.2f}$")
        break
    order_more = input("Would you like to make any other order?")
    if order_more == " no":
        break