def find_food(food):
    food_dict = {'cookie': 'flour', 'cake': 'butter', 'cupcake': 'milk'}
    for k, v in food_dict.items():
        if food == v:
            return str(k)