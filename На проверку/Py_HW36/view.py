from main import *

def show_sales_of_salesman(conn, cursor, sales, salesman):
    conn.commit()
    cursor.execute(f"""SELECT Salesman, Customer, Item, Price
                    FROM {sales.table_name}
                    WHERE Salesman = '{salesman.name} {salesman.surname}'""")
    # for string in sales.table_name:
    # print(cursor.fetchall())