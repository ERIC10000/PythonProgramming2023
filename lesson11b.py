# create a class Book, with the following:
# states: author, title, price, quantity
# methods : show_book(), change_price()

# Get two instances of the class Book:

class Book:
    def __init__(self, author, title, price, quantity): 
        self.author = author
        self.title = title
        self.price = price
        self.quantity = quantity
    
    def show_book(self):
        print(f" Author : {self.author} \n Title : {self.title} \n  Price : {self.price} \n Quantity: {self.quantity}")

    def change_price(self, newPrice):
        self.price = newPrice
        print(f"New Price is : {self.price}")

pearl = Book("Derrick", "The Pearl", 800, 5)
pearl.show_book()
pearl.change_price(1000)
    
