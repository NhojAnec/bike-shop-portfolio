import os

colours = [{"ID" : "[1]", "item" : "White", "price" : "700", "currency" : "THB"},
           {"ID" : "[2]", "item" : "Blue", "price" : "600", "currency" : "THB"},
           {"ID" : "[3]", "item" : "Yellow", "price" : "600", "currency" : "THB"},
           {"ID" : "[4]", "item" : "Black", "price" : "550", "currency" : "THB"},
           {"ID" : "[5]", "item" : "Red", "price" : "500", "currency" : "THB"},
           {"ID" : "[6]", "item" : "Cyan", "price" : "450", "currency" : "THB"},
           {"ID" : "[7]", "item" : "Pink", "price" : "1200", "currency" : "THB"}]

frames = [{"ID" : "[1]", "item" : "Titanium", "price" : "6500", "currency" : "THB"},
          {"ID" : "[2]", "item" : "Steel", "price" : "5750", "currency" : "THB"},
          {"ID" : "[3]", "item" : "Carbon Fiber", "price" : "5500", "currency" : "THB"},
          {"ID" : "[4]", "item" : "Aluminum", "price" : "5000", "currency" : "THB"}]

accessories = [{"ID" : "[1]", "item" : "Headlight", "price" : "500", "currency" : "THB"},
               {"ID" : "[2]", "item" : "Bottle Holder", "price" : "300", "currency" : "THB"},
               {"ID" : "[3]", "item" : "Bell", "price" : "200", "currency" : "THB"},
               {"ID" : "[4]", "item" : "Chibi CEO's keychain", "price" : "200", "currency" : "THB"},
               {"ID" : "[5]", "item" : "No Accessory", "price" : "0", "currency" : "THB"}]

# Rest now my children.
# For you all have done your part.

# def print_colours(input_list):
#     for item in input_list:
#         print(item['ID'], item['colour'], item['price'], item['currency'])

# def print_frames(input_list):
#     for item in input_list:
#         print(item['ID'], item['frame'], item['price'], item['currency'])
price = []
def print_list(input_list):
    for item in input_list:
        print(item['ID'], item['item'], item['price'], item['currency'])
def print_order(input,num):
    print(input[num-1]['ID'], input[num-1]['item'], input[num-1]['price'], input[num-1]['currency'])
def write_texts(input,num):
    write_file.writelines("\t".join((input[num-1]['ID'], input[num-1]['item'], input[num-1]['price'])))
def order_confirm(list):
    price_type = 0
    while True:
        print_list(list)
        print("=" * 20)
        user = input("Please select your option: ")
        if user == "1":
            print("-" * 20)
            print_order(list,1)
            print("-" * 20)
            confirm = input("Confirm your selection? (Y/N):")
            if confirm == 'Y':
                price_type += (float(list[0]['price']))
                write_texts(list,1)
                price.append(price_type)
                print("=" * 20)
                break
            elif confirm == 'N':
                print("=" * 20)
            else:
                print("Please enter correct promt.(Case sensitive)")
                print("=" * 20)
        elif user == "2":
            print("-" * 20)
            print_order(list,2)
            print("-" * 20)
            confirm = input("Confirm your selection? (Y/N):")
            if confirm == 'Y':
                price_type += (float(list[1]['price']))
                write_texts(list,2)
                price.append(price_type)
                print("=" * 20)
                break
            elif confirm == 'N':
                print("=" * 20)
            else:
                print("Please enter correct promt.(Case sensitive)")
                print("=" * 20)
        elif user == "3":
            print("-" * 20)
            print_order(list,3)
            print("-" * 20)
            confirm = input("Confirm your selection? (Y/N):")
            if confirm == 'Y':
                price_type += (float(list[2]['price']))
                write_texts(list,3)
                price.append(price_type)
                print("=" * 20)
                break
            elif confirm == 'N':
                print("=" * 20)
            else:
                print("Please enter correct promt.(Case sensitive)")
                print("=" * 20)
        elif user == "4":
            print("-" * 20)
            print_order(list,4)
            print("-" * 20)
            confirm = input("Confirm your selection? (Y/N):")
            if confirm == 'Y':
                price_type += (float(list[3]['price']))
                write_texts(list,4)
                price.append(price_type)
                print("=" * 20)
                break
            elif confirm == 'N':
                print("=" * 20)
            else:
                print("Please enter correct promt.(Case sensitive)")
                print("=" * 20)
        elif user == "5":
            try:
                print("=" * 20)
                print_order(list,5)
                print("=" * 20)
            except Exception:
                print("Out of Range")
                print("-" * 20)
            else:
                confirm = input("Confirm your selection? (Y/N):")
                if confirm == 'Y':
                    price_type += (float(list[4]['price']))
                    write_texts(list,5)
                    price.append(price_type)
                    print("=" * 20)
                    break
                elif confirm == 'N':
                    print("=" * 20)
                else:
                    print("Please enter correct promt.(Case sensitive)")
                    print("=" * 20)
        elif user == "6":
            try:
                print("=" * 20)
                print_order(list,6)
                print("=" * 20)
            except Exception:
                print("Out of Range")
                print("-" * 20)
            else:
                confirm = input("Confirm your selection? (Y/N):")
                if confirm == 'Y':
                    price_type += (float(list[5]['price']))
                    write_texts(list,6)
                    price.append(price_type)
                    print("=" * 20)
                    break
                elif confirm == 'N':
                    print("=" * 20)
                else:
                    print("Please enter correct promt.(Case sensitive)")
                    print("=" * 20)
        elif user == "7":
            try:
                print("=" * 20)
                print_order(list,7)
                print("=" * 20)
            except Exception:
                print("Out of Range")
                print("-" * 20)
            else:
                confirm = input("Confirm your selection? (Y/N):")
                if confirm == 'Y':
                    price_type += (float(list[6]['price']))
                    write_texts(list,7)
                    price.append(price_type)
                    print("=" * 20)
                    break
                elif confirm == 'N':
                    print("=" * 20)
                else:
                    print("Please enter correct promt.(Case sensitive)")
                    print("=" * 20)
        else:
            print("=" * 20)
            print("Please enter correct action number.")
            print("=" * 20)

write_file = open("./info.txt", "w")
write_file.writelines("ID\t\titem\t\tprice\n")

print("Welcome to SRK's Bike Shop!")
print("=" * 20)
while True:
    print("[1] Contact Us")
    print("[2] About Us")
    print("[3] Order Now")
    print("=" * 20)
    user = input("Please choose your action: ")
    if user == "1":
        print("=" * 20)
        print("Tel: 076543210")
        print("Email: srk@bluearchive.kvt")
        print("Avaliable Time: 08:00 - 20:00")
        print("=" * 20)
    elif user == "2":
        print("=" * 20)
        print("We are SRK's Bike Shop.")
        print("SRK stands for 'Shiroko', our beloved founder from Abydos School, Kivotos.")
        print("=" * 20)
    elif user == "3":
        print("=" * 20)
        break
    else:
        print("=" * 20)
        print("Please enter correct action number.")
        print("=" * 20)

order_confirm(frames)
write_file.writelines("\n")
order_confirm(colours)
write_file.writelines("\n")
order_confirm(accessories)
total = sum(price)
print("Your total price is:",total,"    THB")
print("Thank you for purchasing!")
print("-" * 20)
write_file.writelines("\n===================================")
write_file.writelines(f"\nYour total price is: {total} THB\n------------------------------\nThank you for purchasing!")
write_file.close()