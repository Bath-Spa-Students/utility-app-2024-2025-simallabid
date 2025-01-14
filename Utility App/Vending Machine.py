import time      #importing the time module for delays
import random    #importing the random module for generating random suggestions

# Welcome message for the vending machine
print("ＷＥＬＣＯＭＥ ＴＯ ＳＩＭＡＬ＇Ｓ ＶＥＮＤＩＮＧ ＭＡＣＨＩＮＥ！\n")
time.sleep(1)   #adding a short delay for an effect

#this is the menu for the vending machine
menu = {
    "----------------𝘚𝘕𝘈𝘊𝘒𝘚--------------\n": [
        {"Item Name": "Chips", "Item no.": "1", "Price": 3, "Stock": 5},
        {"Item Name": "Snickers Bar", "Item no.": "2", "Price": 3.5, "Stock": 5},
        {"Item Name": "Pop-Tarts", "Item no.": "3", "Price": 2, "Stock": 5},
        {"Item Name": "Granola Bars", "Item no.": "4", "Price": 2, "Stock": 5},
        {"Item Name": "Cheez-its", "Item no.": "5", "Price": 1.50, "Stock": 5}
    ],
    "----------------𝘋𝘙𝘐𝘕𝘒𝘚--------------\n": [
        {"Item Name": "Juice", "Item no.": "6", "Price": 2.5, "Stock": 5},
        {"Item Name": "Coke", "Item no.": "7", "Price": 3, "Stock": 5},
        {"Item Name": "Water", "Item no.": "8", "Price": 1.5, "Stock": 5},
        {"Item Name": "Coffee", "Item no.": "9", "Price": 5, "Stock": 5},
        {"Item Name": "Tea", "Item no.": "10", "Price": 4, "Stock": 5}
    ],
    "----------------𝘉𝘈𝘒𝘌𝘙𝘠--------------\n": [
        {"Item Name": "Cake", "Item no.": "11", "Price": 6.5, "Stock": 5},
        {"Item Name": "Donut", "Item no.": "12", "Price": 3, "Stock": 5},
        {"Item Name": "Sandwich", "Item no.": "13", "Price": 4, "Stock": 5},
        {"Item Name": "Burger", "Item no.": "14", "Price": 5.5, "Stock": 5},
        {"Item Name": "Croissant", "Item no.": "15", "Price": 2.5, "Stock": 5}
    ]
        
}


#Function is used to display the menu
def display_menu(menu):
    print("---------------𝑴 𝑬 𝑵 𝑼---------------")
    for menu, items in menu.items():    #loop through each menu category 
        print(f"\n{menu}:")             #prints the category name
        for item in items:
            print(f" {item['Item no.']}. {item['Item Name']} - ${item['Price']} - (Stock: {item['Stock']})")  #prints the item detail by using the f-string
    print("\n------------------------------------\n")


#this function is used to find the item by its item number.
def get_item(menu, item_number):
    for items in menu.values():         #loop through all categories
        for item in items:              #loop through each items in the category
            if item["Item no."] == item_number:   #checks if the item number matches
                return item             #returns the matching item
    return None                         #returns nothing id no items match


#this fuction is used to suggest purchases
def suggest_purchase(menu, purchased_items):
    print(f"\nWould you like to buy some ")
    suggestions = [                   #list of items still in stock and not purchased
        item for items in menu.values()
        for item in items if item["Stock"] > 0 and item not in purchased_items
    ]
    if suggestions:
        suggestion = random.choice(suggestions)  #selects a random item
        print(f"- {suggestion['Item Name']} for ${suggestion['Price']}")
    else:
        print("\n- No suggestions available.")


#this is the main vending maching function
def simal_vending_machine():
    balance = 0                               #initializing the user's balance
    purchased_items = []                      #initializing a list to track the purchased items

    while True:                               #infinite loop to keep the vending machine running until the user types done
        display_menu(menu)                    #displays the menu
        user_answer = input("\nEnter the item number to purchase (or type 'done' to exit): ").lower().strip()
        
        if user_answer == 'done':
            print(f"\nYour change of ${balance} is returned.")
            print("\nThank you for using Simal's vending machine!")
            print('\n𝑮𝑶𝑶𝑫𝑩𝒀𝑬 :)')
            break                             #exits the loop if the user types done
        
        item = get_item(menu, user_answer)    #the the item based on the item number
        if item:
            if item["Stock"] <= 0:            #checks if the item is in stock or not
                print(f"\n{item['Item Name']} is out of stock. Sorry for the inconvenience.")
                continue                      #skips the rest of the loop iteration
            
            print(f"\nYou selected {item['Item Name']} for ${item['Price']}.")
            while balance < item["Price"]:    #checks if the balance is insufficient
                try:
                    insert_money = int(input(f"\nInsufficient balance (${balance})! Please insert money: $"))
                    if insert_money > 0:          #checks if the money is positive
                        balance += insert_money   #adds the inserted amount to the balance
                        print(f"\nAdded ${insert_money}.\nCurrent balance:${balance}.")
                    else:
                        print("\nPlease enter a positive amount.")
                except ValueError:
                    print("\nInvalid input. Please enter a valid number.")    #handles invalid input


            #complete the purchase(once the user types done)
            item["Stock"] -= 1           #reduces the stock of the purchased item
            balance -= item["Price"]     #detucts the item's price from the balance
            purchased_items.append(item) #adds the item to the purchased items list
            print(f"\nThank you for purchasing {item['Item Name']}!\nYour remaining balance is: ${balance}")
            suggest_purchase(menu, purchased_items)  #suggests additional purchase
            time.sleep(1)                #short delay for effect
        else:
            print("\nInvalid item number. Please try again.")
        time.sleep(1)


#this runs the vending machine
simal_vending_machine()                  #calls the main vending machine function to start