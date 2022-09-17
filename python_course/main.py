# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {"Jarek"}')  # Press Ctrl+F8 to toggle the breakpoint.
#
# def say_hello():
#     print("hello you from main.py")
#
# def say_hello_with_name(name):
#     print(f"hello, {name}")
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/
# ## zmienne wg python zen nazywamy malymi literami i podkresleniami
# variable= 1
# variable_two = 2
# #stale nazywamy drukowanymi
# VALID = 3.14
# #nie mozna od cyfr zmiennych
from shop.orders import create_new_order

def run_shop():
    print("witaj w sklepie")
    product_name=input("jakie towar chcesz kupic?")
    quantity=int(input("ile sztuk?"))

    result = create_new_order(product_name, quantity)
    if result is not None:
        total_price=result["total_price"]
        print(f"laczny koszt wyniesie {total_price} PLN")

if __name__=='__main__':
    run_shop()