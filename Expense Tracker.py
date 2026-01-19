"""Expense Tracker"""
expenses = {
    "Apple":100,
    "Banana":50,
    "Mango":30,
    "Milk":27,
    "Book":30
}
def add_item(expenses,item,prices):
    expenses[item] = prices
    print(f"{item} added successfully.")


def remove_item(expenses,item):
    if item in expenses:
        del expenses[item]
        print(f"{item} removed successfully.")
    else:
        print("Item not found.")


def claculate_total(expenses):
    total = 0
    for price in expenses.values():
        total += price
    return total


add_item(expenses,"Watermelon",30)
remove_item(expenses,"Book")
total = claculate_total(expenses)
print("Total Expense: ",total)