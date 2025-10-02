from pyscript import display
#Restaurant Order System (Python Data types)

#String
restaurant_name = "Big fry"
owner_name = "Zyan Eusebio"

#Integer
year_since = 2025

#Float
tax_rate = 0.08

#Boolean
has_delivery = True
is_dine_in = True
is_takeaway = False

#List
product_names = ["BBQ fry", "Garlic fry", "Cheese fry"]
beverages = ["Iced Tea" , "Sparkling Water"]

#Tuple
business_hours = ("6:00 AM", "7:00 PM")

#Dictionary
menu = {
    "BBQ fry" : 79.99,
    "Garlic fry" : 65.00,
    "Cheese fry" : 40.00,
    "Iced Tea" : 20.00,
    "Sparkling Water" : 30.00
}

#Set
common_allergens = {"gluten", "dairy", "nuts"}

#Display restaurant info
display(restaurant_name, target="name1")
display(f"Owner: {owner_name}", target="owner")
display(f"Since: {year_since}", target="since")
display(f"Menu Pricelist", target="heading1")

#display menu items
display(product_names[0], target="prod1")
display(f"₱{menu['BBQ fry']:.2f}", target="price1")

display(product_names[1], target="prod2")
display(f"₱{menu['Garlic fry']:.2f}", target="price2")

display(product_names[2], target="prod3")
display(f"₱{menu['Cheese fry']:.2f}", target="price3")

display(product_names[0], target="prod4")
display(f"₱{menu['Iced Tea']:.2f}", target="price4")

display(product_names[1], target="prod5")
display(f"₱{menu['Sparkling Water']:.2f}", target="price5")

#Display additional information
display(f"Open: {business_hours[0]} - {business_hours[1]}", target="openingHours")

#Display order type
display(f"Dine-In Available", target="orderType")