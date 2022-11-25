cook_book = {
  'Омлет': [
    {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
    {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
    {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
    ],
  'Утка по-пекински': [
    {'ingredient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
    {'ingredient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
    {'ingredient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
    {'ingredient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}
    ],
  'Запеченный картофель': [
    {'ingredient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
    {'ingredient_name': 'Чеснок', 'quantity': 3, 'measure': 'зубч'},
    {'ingredient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'},
    ]
  }

"Задание 1 "

"""def cookbook(stuff):
  for x, y in stuff.items():
    print(x)
    print(len(y))
    for w in y:
      print(w['ingredient_name'], '|', w['quantity'], '|', w['measure'])
    print('')


with open('cook_book.txt', 'w') as f:
  f.write(cookbook(cook_book))

with open('cook_book.txt', 'r') as f:
  print(f.readline())




"Задание 2"


def get_shop_list_by_dishes(dishes, person_count):
  for k, v in cook_book.items():
    if k in dishes:
      for item in v:
        print("'",item['ingredient_name'], "':", ": { 'measure' :", item['measure'], "'quantity' :",
              person_count * item['quantity'], '}')



get_shop_list_by_dishes(['Запеченный картофель','Омлет'], 3)

"""



"Задание 3"


files = {'1.txt' : [{'Строка номер' : 1, 'файла номер' : 1},
                   {'Строка номер' : 2, 'файла номер' : 1}],
         '2.txt' : [{'Строка номер': 1, 'файла номер': 2}]
        }




sorted_files = {
    f: sorted(ll, key=lambda x: x['Строка номер'])
    for f, ll in sorted(files.items(), key=lambda x: len(x[1]))
}

for f, ll in sorted_files.items():
    print(f'{f}\n {len(ll)}')
    for l in ll:
        print(' '.join([f'{k} {v}' for k, v in l.items()]))


















'''for x, y in cook_book.items():
  print(x)
  print(len(y))
  for w in y:
    print(w['ingredient_name'],'|',  w['quantity'],'|', w['measure'])
  print('')'''