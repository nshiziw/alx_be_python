class Catalog:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def display_product_information(self):
        information = f"{self.name}, pieces {self.quantity}, each costs {self.price}"
        return information
    
    def display_total_price(self):
        total_price = self.quantity * self.price
        return total_price
    
product = Catalog("BMW", 78000, 3)
print(product.display_product_information())
print(product.display_total_price())