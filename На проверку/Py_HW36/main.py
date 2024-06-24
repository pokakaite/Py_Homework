from models import *
from view import *
import sqlite3

menu = Menu()

def table():
    salesman_1 = Salesman1()
    salesman_2 = Salesman2()
    salesman_3 = Salesman3()

    customer_1 = Customer1()
    customer_2 = Customer2()
    customer_3 = Customer3()

    lamp = Lamp()
    headlight = Headlight()
    xenon = Xenon()

    salesmen = TableSalesmen()
    customers = TableCustomers()
    items = TableItems()

    sales = Table_Sales()

    choices = ChoicesDict()
    make_choice = MakeChoice()

    conn = sqlite3.connect(':memory:')

    cursor = conn.cursor()

    salesmen.create_table(cursor)
    customers.create_table(cursor)
    items.create_table(cursor)

    salesmen.insert_into(conn, cursor, salesman_1)
    salesmen.insert_into(conn, cursor, salesman_2)
    salesmen.insert_into(conn, cursor, salesman_3)

    customers.insert_into(conn, cursor, customer_1)
    customers.insert_into(conn, cursor, customer_2)
    customers.insert_into(conn, cursor, customer_3)

    items.insert_into(conn, cursor, lamp)
    items.insert_into(conn, cursor, headlight)
    items.insert_into(conn, cursor, xenon)

    sales.create_table(cursor)
    sales.insert_into(conn, cursor, salesman_1, customer_1, lamp)
    sales.insert_into(conn, cursor, salesman_1, customer_2, headlight)
    sales.insert_into(conn, cursor, salesman_1, customer_2, xenon)
    sales.insert_into(conn, cursor, salesman_2, customer_3, headlight)
    sales.insert_into(conn, cursor, salesman_3, customer_2, lamp)
    sales.insert_into(conn, cursor, salesman_3, customer_1, lamp)

    ShowChoicesMenu.show(choices.choices)
    make_choice.set_choice()

    match make_choice.get_choice():
        case 1: pass
        case 2: pass
        case 3: pass
        case 4: pass
        case 5: pass
        case 6: pass
        case 7: pass
        case 8: pass
        case 9: pass
        case 10: pass
        case 11: pass
        case 12: pass
        case 13: pass
        case 14: pass

    conn.close()
    return start()

def start():
    menu.show()
    menu.set_choice()
    if menu.choice == 1:
        table()
    else:
        pass

if __name__ == '__main__':
    start()