from models import *
from view import *
from controller import *
import sqlite3

menu = Menu()

def table():
    salesman_1 = Salesman1()
    salesman_2 = Salesman2()
    salesman_3 = Salesman3()

    salesmen = [salesman_1, salesman_2, salesman_3]

    customer_1 = Customer1()
    customer_2 = Customer2()
    customer_3 = Customer3()

    customers = [customer_1, customer_2, customer_3]

    lamp = Lamp()
    headlight = Headlight()
    xenon = Xenon()

    salesmen_table = TableSalesmen()
    customers_table = TableCustomers()
    items_table = TableItems()

    sales = Table_Sales()

    choices = ChoicesDict()
    make_choice = MakeChoice()

    conn = sqlite3.connect(':memory:')

    cursor = conn.cursor()

    salesmen_table.create_table(cursor)
    customers_table.create_table(cursor)
    items_table.create_table(cursor)

    salesmen_table.insert_into(conn, cursor, salesman_1)
    salesmen_table.insert_into(conn, cursor, salesman_2)
    salesmen_table.insert_into(conn, cursor, salesman_3)

    customers_table.insert_into(conn, cursor, customer_1)
    customers_table.insert_into(conn, cursor, customer_2)
    customers_table.insert_into(conn, cursor, customer_3)

    items_table.insert_into(conn, cursor, lamp)
    items_table.insert_into(conn, cursor, headlight)
    items_table.insert_into(conn, cursor, xenon)

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
        case 1: ShowAllSales.show(conn, cursor, sales)
        case 2: (ChooseSalesman.set_choice(salesmen),
                 ShowSalesOneSalesman.show(conn, cursor, sales, salesmen, ChooseSalesman.get_choice()))
        case 3: ShowMaxSumSale.show(conn, cursor, sales)
        case 4: ShowMinSumSale.show(conn, cursor, sales)
        case 5: (ChooseSalesman.set_choice(salesmen),
                ShowMaxSumSaleOneSalesman.show(conn, cursor, sales, salesmen, ChooseSalesman.get_choice()))
        case 6: (ChooseSalesman.set_choice(salesmen),
                ShowMinSumSaleOneSalesman.show(conn, cursor, sales, salesmen, ChooseSalesman.get_choice()))
        case 7: (ChooseCustomer.set_choice(customers),
                ShowMaxSumSaleOneCustomer.show(conn, cursor, sales, customers, ChooseCustomer.get_choice()))
        case 8: (ChooseCustomer.set_choice(customers),
                ShowMinSumSaleOneCustomer.show(conn, cursor, sales, customers, ChooseCustomer.get_choice()))
        case 9: ShowMaxSumSalesOneSalesman.show(conn, cursor, sales)
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