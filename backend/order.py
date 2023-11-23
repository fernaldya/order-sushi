from food import Food

def place_order(food, quantity):
    total_price = food.price * quantity
    print(f"Your order of {quantity} {food.name} will cost {total_price}.")
