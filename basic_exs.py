age = 42

age += 10

divAge = age // 7

textDiv = "{} divided by 7 is equal {}".format(age, divAge)

restDiv = age % 7

expDiv = restDiv ** 3

#user_operation = input("Please write a number : ")

#print(user_operation, type(user_operation))

grocery_items = {
    "butter": 0.77,
    "nutella": 1.87,
    "flour": 0.90,
    "raw cider": 3.85,
    "milk": 0.45
}

orderPrice = grocery_items["butter"] + grocery_items["flour"] + grocery_items["nutella"] + \
             (grocery_items["raw cider"] * 3) + (grocery_items["milk"] * 2)

allowanceMoney = 0

if orderPrice <= allowanceMoney:
    check = allowanceMoney - orderPrice

    print("You have spent {} you have left {}.".format(orderPrice, check))
elif orderPrice > allowanceMoney:
    amountMissing = abs(allowanceMoney - orderPrice)

    print("Sorry you're missing {} euros" .format(amountMissing))

else:
    print("Please put a correct value!")

#number_one = input("First number : ")
#number_two = input("Second number : ")

#minimal_number = min(number_one, number_two)
#print("The smallest number is : ", minimal_number)

#phrase_one = input("First sentence : ")
#phrase_two = input("Second sentence : ")

#minimal_phrase = max(phrase_one, phrase_two)
#print("The largest sentence is : ", minimal_phrase)

# currency = input("Which currency do you want to convert? [€/$] : ")
#
# if currency == "€":
#     print("For 1 euro you can get 1.19 dollar")
#     money_euro = float(input("How many euros do you have? "))
#     exchange_euro = money_euro * 1.19
#     print("For {}€ you can have {}$".format(money_euro, exchange_euro))
# elif currency == "$":
#     print("For 1 dollar you can get 0.84 euro")
#     money_dollar = float(input("How many dollars do you have? "))
#     exchange_dollar = money_dollar * 0.84
#     print("For {}€ you can have {}$".format(money_dollar, exchange_dollar))
# else:
#     print("Please choose € or $ ")

# studentsTuring = ["Redouane", "Justine", "Ruben", "Edouard"]
# name = "Julie"
#
# if name in studentsTuring:
#     print("You are at the turing's")
# else:
#     print("You are not part of the turing's")

import math
sphere_radius = 10

sphere_volume = ((4/3)*math.pi) * sphere_radius**3

print("The volume of a sphere with a radius of {} is : {}".format(sphere_radius, sphere_volume))
