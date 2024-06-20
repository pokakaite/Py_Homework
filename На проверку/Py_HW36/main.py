from salesmen import *
from customers import *
from items import *
from sales import *
from view import *
import sqlite3

salesman_1 = Salesman_1()
salesman_2 = Salesman_2()
salesman_3 = Salesman_3()

customer_1 = Customer_1()
customer_2 = Customer_2()
customer_3 = Customer_3()

lamp = Lamp()
headlight = Headlight()
xenon = Xenon()

salesmen = Table_Salesmen()
customers = Table_Customers()
items = Table_Items()

sales = Table_Sales()

conn = sqlite3.connect(':memory:')

if __name__ == '__main__':
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

    sales.show_all(conn, cursor)
    show_sales_of_salesman(conn, cursor, sales, salesman_1)

    conn.close()