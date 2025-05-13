min_age = 5
max_age = 17
transport_cost = 80

# First name and age
camper_name =input("What is you full name?")
age = int(input("How old are you?"))
#if age is between 5 and 17 you can do it but if younger or older then that you are too older or young to do it
if age < min_age:
    print("Sorry you are to young to join the camp")
if age > max_age:
    print("Sorry you are to old to join the camp")
if age > 15:
    input("Do you want to be a camp leader at the camp you choose to be at?")

# Choosing a activity to do
activity_cost =[800, 400, 900]
chosen_activity = ["Cultural Immersion (5 days, easy, $800 fee)","Kayaking and Pancake (3 days, moderate, $400 fee)", "Mountain biking (4 Days, difficult, $900 fee)"]
print("Choose an activity")
print(f"1. {chosen_activity[0]}")
print(f"2. {chosen_activity[1]}")
print(f"3. {chosen_activity[2]}")
chosen_activity = int(input("Enter the number of your chosen activity:"))
print("Choose one of the activity to do:")
if chosen_activity == 1:
    camp_cost = 800
elif chosen_activity == 2:
    camp_cost = 400
elif chosen_activity == 3:
    camp_cost = 900


if chosen_activity == 1:
    name_of_activity = "Cultural Immersion (5 days, easy, $800 fee)"
elif chosen_activity == 2:
    name_of_activity = "Kayaking and Pancake (3 days, moderate, $400 fee)"
elif chosen_activity == 3:
    name_of_activity = "Mountain biking (4 Days, difficult, $900 fee)"


#choosing Meal options 
meal_options = ["Standard", "Vegetarian", "Vegan"]
print("Choose a Meal")
print(f"1. {meal_options[0]}")
print(f"2. {meal_options[1]}")
print(f"3. {meal_options[2]}")
meal_option = int(input("Enter the number of your choice meal"))

if meal_options == 1:
    name_of_meal = "Standard"
elif meal_option == 2:
    name_of_meal = "Vegetarian"
elif meal_option == 3:
    name_of_meal = "Vegan"

# Asking if you need a shuttle bus to get to the camp 
while True:
    shuttle_bus = input("Will you be needing a shuttle bus to get there? it will cost $80. Please enter y/yes or n/no: ")
    shuttle_bus = shuttle_bus.lower()
    if shuttle_bus == "yes" or shuttle_bus == "no" or shuttle_bus == "y" or shuttle_bus == "n":
        break
    else:
        print("Please enter either Yes if youd like to get on the shuttle bus to get there for $80, or no if you will be driving there yourself.")
 
#outcome of the question above
if shuttle_bus == "yes" or shuttle_bus == "y":
    print("Picked yes for shuttle bus + $80")
    print("Thank you!")
elif shuttle_bus == "no" or shuttle_bus == "n":
    print("no shuttle bus!")
    print("This means you will have to drive there yourself!")
 
#Sets the price for the shuttle bus
if shuttle_bus == "yes" or shuttle_bus == "y":
    transport_cost = 80
    bus_answer = "yes"
elif shuttle_bus == "no" or shuttle_bus == "n":
    transport_cost = 0
    bus_answer = "no"

if chosen_activity == 1:
    print(f"your name is {camper_name}, you are {age} years old, the activity you choose was {name_of_activity}, your meal option you choose was {name_of_meal}. the total cost is ${activity_cost[0] + transport_cost}")
elif chosen_activity == 2:
    print(f"your name is {camper_name}, you are {age} years old, the activity you choose was {name_of_activity}, your meal option you choose was {name_of_meal}. the total cost is ${activity_cost[1] + transport_cost}")
elif chosen_activity == 3:
    print(f"your name is {camper_name}, you are {age} years old, the activity you choose was {name_of_activity}, your meal option you choose was {name_of_meal}. the total cost is ${activity_cost[2] + transport_cost}")





while True:
    final_decision = input(f"Do you want to proceed with the payment of the ${camp_cost + transport_cost} (yes/no): ")
    if len(final_decision) == 0:
        print("Invalid input. Please enter yes or no")
    elif final_decision.lower() in ['yes' , 'y']:
        print("Payment accepted. Thank you!")
        exit()
    elif final_decision.lower() in ['no' , 'n']:
        print("Payment cancelled.")
        exit() 