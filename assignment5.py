print("--------------------QUESTION 1------------------------\n\n")
#program to create a dictionary with personal data
yourself={
    "first_name":"sai","last_name":"govid","age":"24","city":"ottawa","fav_toppings":"chicken","hobby":"gaming"
}
for dictionary in yourself.items():
    print(dictionary)
print("--------------------QUESTION 2------------------------\n\n")
#program to store five classmate names and their fav food items
classmates = {
    "sai":["pizza","burger","rice"],
    "alex":["cheese burger","curd rice","pizza"],
    "ajith":["chiken wings","porotta","manthi","burger"],#list is adding by the help of []
    "john":["fish fry","chicken tikka masala","pasta"],
    "mark":["ice cream","coffee","cake"]
}
for friends in classmates:
    print(f"name of friend is {friends} and fav foods are {classmates[friends]} ")
print("--------------------QUESTION 3------------------------\n\n")
#progarm to create multiple dictionarys and store in a list

person1={'name':'sai','food':'biriyani','meal':'curd'}
person2={'name':'alex','food':'lamb','meal':'vegetable'}
person3={'name':'ajith','food':'beef','meal':'bread'}
person4={'name':'anto','food':'fish','meal':'rice'}
meals=[person1,person2,person3,person4]
for person in meals:
    name=person['name']
    food=person['food']
    meal=person['meal']
    print(f"{name} favirate food combination are {food} and {meal}")

print("--------------------QUESTION 4------------------------\n\n")
#program to make a dictionary inside a dictionay
cities={
    'alappuzha':{'city_name':'alappuzha','country':'India','population':'800000','fact':{"seaside area in india","land of five lamps","alappuzha is surrounded with backwaters"}},
    'ottawa':{'city_name':'ottawa','country':'canada','population':'500000','fact':{"Ottawa is Canada capital","There are more than 14 museums in Ottawa","Ottawa is the seventh coldest capital in the world"}},
    'dublin':{'city_name':'dublin','country':'ireland','population':'30000','fact':{"capital of the Republic of Ireland","Dublin is a warm and welcoming city","centre of financial and commercial power"}}
}
for city, info in cities.items():
    print(f"\n{city}:")
    for key, value in info.items():
        if isinstance(value, list):
            print(f"{key}:")
            for fact in value:
                print(f"  - {fact}")
        else:
            print(f"{key}: {value}")
print("--------------------QUESTION 5------------------------\n\n")
#program to create dictionary stock prices and name three cities
# Define the stock prices dictionary
stock_prices = {
    "apple": [150.2, 151.5, 149.8, 152.3, 148.6, 150.7, 153.0, 151.2, 149.1, 152.5],
    "python": [2750.3, 2765.8, 2748.1, 2772.6, 2739.2, 2756.7, 2768.4, 2749.9, 2771.0, 2745.5],
    "flipcart": [3400.2, 3412.7, 3398.9, 3415.6, 3387.3, 3402.8, 3421.5, 3395.7, 3418.1, 3382.6]
}

# Loop through each stock
for stock, prices in stock_prices.items():
    minimum = min(prices)
    maximam = max(prices)
    average = sum(prices) / len(prices)

    # Print information for each stock
    print(f"\nStock: {stock}")
    print(f"Minimum Price: {minimum}")
    print(f"Average Price: {average:.2f}")
    print(f"Maximum Price: {maximam}")
print("--------------------QUESTION 6------------------------\n\n")
import random
populatity=0
for event in range(1,5+1):
    gain=int(random.uniform(1,20))
    populatity=int(populatity+gain)
    print(f"Event {event} is happen")
    print(f"something importent is happen and gains popularity  {gain}% Then, the overall popularity is {populatity}%\n")
if populatity>51:
    print(f"the candidate win the election with {populatity}% popularity\n")
elif populatity<=51:
    print(f"The candidate loose the election with {populatity}% popularity\n")        

print("--------------------QUESTION 7------------------------\n\n")
#program to create dictionary of data types
dic={
    "int":"123456789",
    "float":"7.99",
    "string":"Sai govid",
    "list":"[myself,sai,govid]",
    "dictionary":{'lan1':'python','lan2':'java','lan3':'c++'},
    "tuple":("amazon","flipkart","apple")
}
for data in dic:
    print("datatype is",data,"and value is",dic[data])