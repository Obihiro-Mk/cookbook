from pprint import pprint
cook_book = {}

with open('recipes.txt', 'r', encoding='utf-8') as file:
    while True:
        dish = file.readline().strip()
        if dish == '':
            break
        counter = int(file.readline())
        ing_list = []
        for quantity in range(counter):
            dict_ing = {}
            ingredients = file.readline().strip().split('|')
            dict_ing = {'ingredient_name': ingredients[0], 'quantity': int(ingredients[1]),
                                'measure': ingredients[2]}
            ing_list.append(dict_ing)
        cook_book[dish] = ing_list
        file.readline()
pprint(cook_book)

def get_shop_list_by_dishes(dishes, person_count):
    dish_person = {}
    for d in dishes:
        if d in cook_book.keys():
            for ds in cook_book[d]:
                if ds['ingredient_name'] not in dish_person.keys():
                    dish_person[ds['ingredient_name']] = {'measure': ds['measure'],
                                                          'quantity': ds['quantity'] * person_count}
                else:
                    q = ds['quantity'] * person_count
                    dish_person[ds['ingredient_name']] = {'measure': ds['measure'],
                                                          'quantity': ds['quantity'] * person_count + q}
    pprint(dish_person)

get_shop_list_by_dishes(['Какое-то', 'Омлет'], 2)


