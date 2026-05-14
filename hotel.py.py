"""The smart cafe ordering"""
pizza_count = 0
pasta_count = 0
Burger_count = 0
Coffe_count = 0
Tea_count  = 0
total_bill = 0
discount = 0 
while True:
    print('"-----Menu-----"')
    print("1.pizza(rs200)")
    print("2.pasta(rs150)")
    print("3.Burger(rs100)")
    print("4.coffe(rs100)")
    print("5.Tea(rs50)")
    print("6.Generate Bill and Exit")
   
    print("-------Welcome To Smart Cafe--------")
    choice = int(input("enter the choice: "))
    match choice:
        case 1:
            total_bill +=200
            pizza_count +=1
            print("Added pizza to order")
            
            print()            
        case 2:
            total_bill+=150
            pasta_count+=1
            print("Added pasta to order")
            print()            
        case 3:
            total_bill+=100
            Burger_count+=1
            print("Added Burger to order")
            print()        
        case 4:
            total_bill+=100
            Coffe_count+=1
            print("Added Coffe to order")
            print()            
        case 5:
            total_bill+=50
            Tea_count +=1
            print("Added Tea to order")
            print()          
        case 6:
            break        
        case _: 
            print("Wrong Choice Try Again :)") 
if total_bill>100:
    print ("You got a 10% discount for spending over rs 100")
    discount= total_bill*0.1
final_amount =  total_bill - discount                            
print("-----Final Receipt-------")
if  pizza_count>0:
    print(f"Pizza:{pizza_count}plate")
if  pasta_count>0:
    print(f"pasta:{pasta_count}plate")
if  Burger_count>0:
    print(f"Burger:{Burger_count}plate") 
if  Coffe_count>0:
    print(f"Coffe:{Coffe_count}cup")
if  Tea_count>0:
    print(f"Tea:{Tea_count}cup")
print("-------------------------")    
print(f"Total Bill : RS{total_bill}")
print(f"Discount : RS{discount}")
print(f"Final Amount:Rs{final_amount}") 
print("-------------------------")
print("Thank you For Visiting :)")   
                    
            
    