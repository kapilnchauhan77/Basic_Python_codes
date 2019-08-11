class Customer(object):
    def __init__(self):
        self.customer_number = 111
        self.customer_name = 'Leena'
        self.price = 0
        self. quantity = 0
        self.discount = 0
        self.net_price = 0
        self.total_price = 0

    def caldiscount(self):
        self.total_price = self.price * self.quantity
        if self.total_price >= 50000:
            self.discount = (25/100)*self.total_price
        elif self.total_price in range(25000, 50000):
            self.discount = (15/100)*self.total_price
        elif self.total_price < 25000:
            self.discount = (10/100)*self.total_price
        else:
            pass
        self.net_price = self.total_price - self.discount

    def input(self):
        self.customer_name = input('Please enter name of the customer: ')
        self.customer_number = input('Please enter customer number: ')
        self.price = int(input('Please enter the price of the product to be purchased: '))
        self.quantity = int(input('Please enter the quantity of the product to be purchased: '))

    def show(self):
        print('Name of the customer:', self.customer_name)
        print('Customer numer:', self.customer_number)
        print('Price of the individual product:', self.price)
        print('Quantity of product purchased:', self.quantity)
        print('Total price without discount:', self.total_price)
        print('Discount applied:', self.discount)
        print('Net price of the purchase with discount applied:', self.net_price)


customer = Customer()
customer.input()
customer.caldiscount()
customer.show()
