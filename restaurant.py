class Restaurant:
    def __init__(self):
        self.menu_items = []
        self.booked_tables = []
        self.orders = []

    def add_item_to_menu(self, item_name):
        self.menu_items.append(item_name)

    def book_table(self, table_number):
        self.booked_tables.append(table_number)

    def customer_order(self, order_details):
        self.orders.append(order_details)

    def print_menu(self):
        print("Menu Items:", self.menu_items)

    def print_table_reservations(self):
        print("Table Reservations:", self.booked_tables)

    def print_customer_orders(self):
        print("Customer Orders:", self.orders)

restaurant = Restaurant()
restaurant.add_item_to_menu("Pizza")
restaurant.add_item_to_menu("Burger")
restaurant.book_table(1)
restaurant.book_table(2)
restaurant.customer_order("Pizza for Table 1")
restaurant.customer_order("Burger for Table 2")

restaurant.print_menu()
restaurant.print_table_reservations()
restaurant.print_customer_orders()
