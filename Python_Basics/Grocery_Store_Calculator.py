# Write a program which will keeep adding a sring of numbers inputed by the users the ading stops as soon as user presses q key on keyboard?

sum = 0
Buying_item_list = []
Buying_item_price = []
while(True):
    user_item_input = input("Enter the item name or press q to quit: ")
    user_price_input = input("Enter the item price or press q to quit: ")
    if (user_item_input and user_price_input !='q'):
        Buying_item_list.append(user_item_input)
        Buying_item_price.append(user_price_input)
        sum = sum + int(user_price_input)
        print(f"order total so far {sum}")
    else:
        print(f"your total bill is {sum}")
        print("Thanks for shopping with us.")
        break
print("Your total items are: ", len(Buying_item_list),Buying_item_list)
print("Your total bill is: ",sum)
print("======================Summery=======================")
print("The imaginary store.")
print("Sr.No.", "    ","Item Name.","  ", "Item Price")
for item in range(1,len(Buying_item_list)+1):
    print(" ",item, "         ",Buying_item_list[item-1],"          ",Buying_item_price[item-1])
print(20 * "--")
print("           ","Total amount: ", sum)
print("======Thank You Visit Again======")
