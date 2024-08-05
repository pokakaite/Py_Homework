from models import *
from view import *
from controller import *
import sqlite3

def table():
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()

    menu = Menu()

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

    items = [lamp, headlight, xenon]

    salesmen_table = TableSalesmen()
    customers_table = TableCustomers()
    items_table = TableItems()

    sales = Table_Sales()

    choices = ChoicesDict()
    make_choice = MakeChoice()

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

    choose_salesman = ChooseSalesman(salesmen)
    choose_customer = ChooseCustomer(customers)
    choose_item = ChooseItem(items)
    set_salesman = SetSalesmanName()
    set_customer = SetCustomerName()
    set_item = SetItem()
    set_price = SetPrice()


    show_all_sales = ShowAllSales(conn, cursor, sales)
    show_sales_one_salesman = ShowSalesOneSalesman(conn, cursor, sales)
    show_max_sum_sale = ShowMaxSumSale(conn, cursor, sales)
    show_min_sum_sale = ShowMinSumSale(conn, cursor, sales)
    show_max_sum_sale_one_salesman = ShowMaxSumSaleOneSalesman(conn, cursor, sales)
    show_min_sum_sale_one_salesman = ShowMinSumSaleOneSalesman(conn, cursor, sales)
    show_max_sum_sale_one_customer = ShowMaxSumSaleOneCustomer(conn, cursor, sales)
    show_min_sum_sale_one_customer = ShowMinSumSaleOneCustomer(conn, cursor, sales)
    show_one_salesman_max_sum_sales = ShowOneSalesmanMaxSumSales(conn, cursor, sales)
    show_one_salesman_min_sum_sales = ShowOneSalesmanMinSumSales(conn, cursor, sales)
    show_one_customer_max_sum_sales = ShowOneCustomerMaxSumSales(conn, cursor, sales)
    show_one_customer_min_sum_sales = ShowOneCustomerMinSumSales(conn, cursor, sales)
    show_avg_sum_sales_one_salesman = ShowAvgSumSalesOneSalesman(conn, cursor, sales)
    show_avg_sum_sales_one_customer = ShowAvgSumSalesOneCustomer(conn, cursor, sales)


    def show():
        ShowChoicesMenu.show(choices.choices)
        make_choice.set_choice()

        match make_choice.get_choice():
            case 1:
                show_all_sales.show(),
                show_all_sales.show_table()
            case 2:
                choose_salesman.set_choice(),
                show_sales_one_salesman.show(choose_salesman.get_name()),
                show_sales_one_salesman.show_table()
            case 3:
                show_max_sum_sale.show()
                show_max_sum_sale.show_table()
            case 4:
                show_min_sum_sale.show()
                show_min_sum_sale.show_table()
            case 5:
                choose_salesman.set_choice(),
                show_max_sum_sale_one_salesman.show(choose_salesman.get_name()),
                show_max_sum_sale_one_salesman.show_table()
            case 6:
                choose_salesman.set_choice(),
                show_min_sum_sale_one_salesman.show(choose_salesman.get_name()),
                show_min_sum_sale_one_salesman.show_table()
            case 7:
                choose_customer.set_choice(),
                show_max_sum_sale_one_customer.show(choose_customer.get_name()),
                show_max_sum_sale_one_customer.show_table()
            case 8:
                choose_customer.set_choice(),
                show_min_sum_sale_one_customer.show(choose_customer.get_name()),
                show_min_sum_sale_one_customer.show_table()
            case 9:
                show_one_salesman_max_sum_sales.show()
            case 10:
                show_one_salesman_min_sum_sales.show()
            case 11:
                show_one_customer_max_sum_sales.show()
            case 12:
                show_one_customer_min_sum_sales.show()
            case 13:
                choose_salesman.set_choice(),
                show_avg_sum_sales_one_salesman.show(choose_salesman.get_name()),
            case 14:
                choose_customer.set_choice(),
                show_avg_sum_sales_one_customer.show(choose_customer.get_name()),

        conn.close()
        return table()


    def update():
        update_data = UpdateData(conn, cursor, sales)

        show_all_sales.show()
        show_all_sales.show_table()
        choose_salesman.set_choice()
        set_salesman.set_name()

        choose_customer.set_choice()
        set_customer.set_name()

        choose_item.set_choice()
        set_item.set_item()

        set_price.set_price()

        update_data.update(choose_salesman.get_name(), set_salesman.get_name(),
                           choose_customer.get_name(), set_customer.get_name(),
                           choose_item.get_item(), set_item.get_item(),
                           set_price.get_price())

        show_all_sales.show()
        show_all_sales.show_table()
        return start()

    def add():
        add_data = AddData(conn, cursor, sales)

        show_all_sales.show()
        show_all_sales.show_table()

        set_salesman.set_name()
        set_customer.set_name()
        set_item.set_item()
        set_price.set_price()

        add_data.add(set_salesman.get_name(), set_customer.get_name(),
                     set_item.get_item(), set_price.get_price())

        show_all_sales.show()
        show_all_sales.show_table()
        return start()

    def delete():
        delete_data = DeleteData(conn, cursor, sales)

        show_all_sales.show()
        show_all_sales.show_table()

        choose_salesman.set_choice()
        choose_customer.set_choice()
        choose_item.set_choice()
        set_price.set_price()
        delete_data.delete(choose_salesman.get_name(), choose_customer.get_name(),
                           choose_item.get_item(), set_price.get_price())

        show_all_sales.show()
        show_all_sales.show_table()
        return start()


    def start():
        menu.set_choice()
        match menu.get_choice():
            case 1:
                show()
            case 2:
                update()
            case 3:
                add()
            case 4:
                delete()
            case 5:
                pass

    start()

if __name__ == '__main__':
    table()
