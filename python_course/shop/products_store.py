products ={
"chleb":{
    "quantity":100,
    "price": 3.5 },
"jablka":{
    "quantity":50,
    "price": 3.2
}}


def update_products_quantity(products_name, ordered_quantity):
    products[products_name]["quantity"]-=ordered_quantity

