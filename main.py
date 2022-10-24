cook_book = {}

with open('cook_book.txt', 'rt', encoding='utf8') as file:
    for l in file:
        dish_name = l.strip()
        ingridients = []
        ingridients_count = file.readline()
        for i in range(int(ingridients_count)):
            ing = file.readline()
            ing.split('|')
            ingredient_name, quantity, measure = ing.strip().split('|')
            ingridients.append({'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure})
        blank_line = file.readline()
        cook_book.update({dish_name: ingridients})

print(f'cook_book = {cook_book}\n')


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        if dish in cook_book.keys():
            for ing in cook_book[dish]:
                sum_1 = int(ing['quantity']) * person_count
                shop_list.update({ing['ingredient_name']: {'measure': ing['measure'], 'quantity': sum_1}})
    return shop_list


print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))


import os

lin_1 = {}
for file in os.listdir('files'):
  with open(os.path.join('files', file), encoding='utf-8') as f:
    text = f.readlines()
    text_ = "".join(text)
    len_ = len(text)
    lin_1[file] = (f'{len_}\n{text_}\n')
#print(lin_1)
lin_2 = {}
for x in sorted(lin_1, key=lin_1.get):
  lin_2[x] = lin_1[x]
text_dict = {}
for key, value in lin_2.items():
  with open('new.txt', 'a', encoding='utf-8') as f:
    f.writelines(f'{key}\n{value}\n')
# file.close()


