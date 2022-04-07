from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

def print_report():
    coffee_maker.report()
    money_machine.report()

while True:
    options = menu.get_items()
    choice = input(f"What would you like? ( {options} ) :")
    if choice == "off":
        break
    if choice == "report":
        print_report()
        continue

    drink = menu.find_drink(choice)
    if not coffee_maker.is_resource_sufficient(drink):
        continue
    if not money_machine.make_payment(drink.cost):
        continue
    coffee_maker.make_coffee(drink)


