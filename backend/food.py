class Food():
    def __init__(self, food, quantity):
        self.food = food
        self.quantity = quantity

    def __str__(self):
        order = {
            'menu': self.food,
            'quantity': self.quantity
        }
        return order