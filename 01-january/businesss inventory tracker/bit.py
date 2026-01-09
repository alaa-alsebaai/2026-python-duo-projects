import os
import csv
import sys

exitsys = 0


def file_init():
    if not os.path.exists("items.csv"):
        with open("items.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Name", "Quantity", "Price", "Total"])


def load_expenses():
    expenses = {}
    with open("items.csv", mode="r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            expenses[row["Name"]] = {
                "quantity": int(row["Quantity"]),
                "price": float(row["Price"]),
                "total": float(row["Total"])
            }
    return expenses


def save_expenses(expenses):
    with open("items.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Quantity", "Price", "Total"])
        for name, details in expenses.items():
            writer.writerow([name, details["quantity"],
                            details["price"], details["total"]])


def add_expenses(name, quantity, price):
    expenses = load_expenses()
    expenses[name] = {"quantity": quantity,
                      "price": price, "total": price * quantity}
    print("Item added successfully!\n")
    save_expenses(expenses)


def update_quantities(name, change, price):
    expenses = load_expenses()
    expenses[name]['quantity'] += change
    expenses[name]['total'] = price * expenses[name]['quantity']
    print(f"{change} {name}/s have been added!\n")
    save_expenses(expenses)


def sell_expenses(name, change, price):
    expenses = load_expenses()
    expenses[name]['quantity'] -= change
    expenses[name]['total'] = price * expenses[name]['quantity']
    print(f"{change} units sold! \n")
    save_expenses(expenses)


def view_inventory():
    expenses = load_expenses()
    for name, details in expenses.items():
        print(
            f"{name}: {details['quantity']} units, Total = ${details['total']:.2f}")


while exitsys == 0:
    file_init()
    print("="*40)
    print("Welcome to your Business Expense Tracker\nPlease select an action")
    print("1-View Inventory\n2-Add Item\n3-Update Quantity\n4-Sell Stock\n5-Quit Program")

    while True:
        try:
            action = int(input("Action: "))
            if action < 1 or action > 5:
                print("Please enter a number between 1 and 5")
                continue
            break
        except ValueError:
            print("Enter an actual number. \n")
            continue

    if action == 1:
        expenses = load_expenses()
        if expenses:
            print("Your inventory: \n")
            view_inventory()
        else:
            print("No items in stock. \n")
            continue

    elif action == 2:
        expenses = load_expenses()
        while True:
            name = input("Item: ").strip()
            if not name:
                print("Please enter a non-empty item name.\n")
                continue
            if name.isdigit():
                print("Please enter an actual name (not a number).\n")
                continue
            name = name.capitalize()
            break
        if name in expenses:
            print("Item already in stock.\n")
            continue
        else:
            while True:
                try:
                    quantity = int(input("Quantity? "))
                    if quantity < 0:
                        print("Quantity must be non-negative.")
                        continue
                    break
                except ValueError:
                    print("Enter a valid number.")
            while True:
                try:
                    price = int(input("At what price? "))
                    if price < 0:
                        print("Price must be non-negative.")
                        continue
                    break
                except ValueError:
                    print("Enter a valid number.")
            add_expenses(name, quantity, price)

    elif action == 3:
        expenses = load_expenses()
        print("Which item would you like to add to? ")
        for name in expenses:
            print(name)
        while True:
            name = input("Item: ").strip()
            if not name:
                print("Please enter an item. \n")
                continue
            if name.isdigit():
                print("Please enter an actual name (not a number). \n")
                continue
            name = name.capitalize()
            if name not in expenses:
                print("Please enter an item that is in stock. \n")
                continue
            break
        while True:
            try:
                change = int(input("How much would you like to add? "))
                if change < 0:
                    print("Please enter a non-negative number. \n")
                    continue
                break
            except ValueError:
                print("Please enter a valid number.")
        price = expenses[name]['price']
        update_quantities(name, change, price)
    elif action == 4:
        expenses = load_expenses()
        print("Which item would you like to sell? ")
        for name, details in expenses.items():
            print(f"{name}: quantity: {details['quantity']}")
        while True:
            name = input("Item: ").strip()
            if not name:
                print("Please enter an item. \n")
                continue
            if name.isdigit():
                print("Please enter an actual item(not a number). \n")
                continue
            name = name.capitalize()
            if name not in expenses:
                print("Please enter an item in stock. \n")
                continue
            break
        while True:
            try:
                change = int(input("How much would you like to sell? "))
            except ValueError:
                print("Please enter an actual number. \n")
            if change > expenses[name]['quantity']:
                print("You can't sell more than you have! \n")
                print(f"{name}: quantity: {expenses[name]['quantity']}")
                continue
            break
        price = expenses[name]['price']
        sell_expenses(name, change, price)

    elif action == 5:
        confirm = 0
        while confirm == 0:
            print("Are you sure you want to quit?")
            answer = input("Y/n: ").strip()
            if answer.lower() in ("y", "yes"):
                print("See you next time!")
                sys.exit(0)
            elif answer.lower() in ("n", "no"):
                confirm += 1
                continue
            else:
                print("Enter Y/n")
                continue
