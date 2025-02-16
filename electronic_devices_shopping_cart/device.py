class Device:
    def __init__(self, name, price, stock, warranty_period=12):
        self.name = name
        self.price = price
        self.stock = stock
        self.warranty_period = warranty_period

    # Displays the basic details of the device (name, price, stock, warranty).
    def display_info(self):
        return f'Name: {self.name}, Price: {self.price}, Stock: {self.stock}, Warranty period: {self.warranty_period} months'

    # Reduces the price by a specified discount percentage.
    def apply_discount(self, discount_percentage):
        self.price -= self.price * (discount_percentage / 100)

    # Checks if the device is available in the required quantity
    def is_available(self, amount):
        return amount <= self.stock

    # Reduces the stock by the specified quantity when a purchase is made
    def reduce_stock(self, amount):
        if self.is_available(amount):
            self.stock -= amount
            return True
        return False
